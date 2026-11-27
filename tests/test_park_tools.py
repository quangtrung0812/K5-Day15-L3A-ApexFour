"""Kiểm ràng buộc lịch trình trên dữ liệu SunWonder Mẫu."""

from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "codebase"))
import tools
import tracing


SUNNY = "2026-11-28"
RAINY = "2026-11-29"


def activity(point_id, start, end):
    return {"diem_id": point_id, "bat_dau": start, "ket_thuc": end}


class ParkToolsTest(unittest.TestCase):
    def check(self, itinerary, budget=2_770_000, **kwargs):
        return tools.kiem_lich_trinh(
            itinerary, 2, 1, kwargs.pop("ages", [7]), budget,
            kwargs.pop("weather", {"ngay": SUNNY}), **kwargs,
        )

    def assert_errors(self, result, *errors):
        self.assertFalse(result["hop_le"])
        self.assertEqual({error["ma"] for error in result["loi"]}, set(errors))

    def test_lookup_and_exact_budget_at_walking_boundary(self):
        tracing.begin("cp2-tools")
        try:
            points = tools.tra_diem_choi("Z1", [3], True)
            self.assertEqual({point["id"] for point in points}, {"A01", "A04", "A14"})
            self.assertEqual(len(tools.tra_lich_show(SUNNY)), 5)
            weather = tools.tra_thoi_tiet(SUNNY)
            self.assertIsNone(weather["rain_from"])
            self.assertEqual(tools.uoc_thoi_gian_di("A07", "S02"), 5)
            result = self.check([
                activity("S02", "11:00", "11:20"),
                {**activity("A07", "10:15", "10:55"), "tien": 1},
            ], weather=weather)
            self.assertTrue(result["hop_le"])
            self.assertEqual(result["tong_tien"], 2_770_000)
            self.assertEqual(result["tien_ve_cong"], 2_420_000)
        finally:
            summary, _ = tracing.end()
        self.assertEqual(summary["tool_calls"], 5)

    def test_over_budget_and_insufficient_walk(self):
        result = self.check([
            activity("A07", "10:16", "10:56"),
            activity("S02", "11:00", "11:20"),
        ], budget=2_769_999)
        self.assert_errors(result, "KHONG_DU_GIO_DI_BO", "VUOT_NGAN_SACH")
        conflict = self.check([activity("S01", "10:30", "11:00"), activity("S02", "11:00", "11:20")])
        self.assert_errors(conflict, "KHONG_DU_GIO_DI_BO")
        self.assertEqual(conflict["loi"][0]["can_phut"], 12)

    def test_park_and_activity_hours_overlap_and_maintenance(self):
        self.assert_errors(self.check([
            activity("A01", "08:00", "09:30"),
            activity("A09", "09:00", "09:45"),
        ], khung_gio={"bat_dau": "09:00", "ket_thuc": "17:00"}),
            "NGOAI_GIO_CHUYEN_DI", "NGOAI_GIO_MO_CUA", "BAO_TRI", "TRUNG_GIO")
        self.assert_errors(self.check([activity("A12", "16:00", "16:40")]),
                           "NGOAI_GIO_MO_CUA", "KHONG_DU_THOI_LUONG")

    def test_show_cancellation_and_fixed_time(self):
        show = activity("S04", "16:15", "16:45")
        rainy_shows = {slot["id"]: slot for slot in tools.tra_lich_show(RAINY)}
        self.assertTrue(rainy_shows["S04"]["huy"])
        self.assertFalse(rainy_shows["S03"]["huy"])
        self.assert_errors(self.check([show], weather={"ngay": RAINY}),
                           "SUAT_SHOW_KHONG_CO_HOAC_DA_HUY", "MUA_NGOAI_TROI")
        self.assert_errors(self.check([show], show_da_huy=["S04"]), "SUAT_SHOW_KHONG_CO_HOAC_DA_HUY")
        self.assert_errors(
            self.check([show], show_da_huy=[{"diem_id": "S04", "bat_dau": "16:15"}]),
            "SUAT_SHOW_KHONG_CO_HOAC_DA_HUY",
        )
        self.assert_errors(self.check([activity("S04", "16:16", "16:46")]),
                           "SUAT_SHOW_KHONG_CO_HOAC_DA_HUY")

    def test_midday_rain_and_manual_cancellation_agree_with_lookup(self):
        cancellations = [{"diem_id": "S03", "bat_dau": "15:00"}]
        shows = {
            slot["id"]: slot for slot in tools.tra_lich_show(
                SUNNY, mua_tu="11:00", show_da_huy=cancellations,
            )
        }
        self.assertEqual({show_id for show_id, slot in shows.items() if slot["huy"]},
                         {"S03", "S04", "S05"})
        weather = {"ngay": SUNNY, "mua_tu": "11:00"}
        self.assert_errors(
            self.check([activity("S03", "15:00", "15:20")], weather=weather,
                       show_da_huy=cancellations),
            "SUAT_SHOW_KHONG_CO_HOAC_DA_HUY",
        )
        replacement = self.check(
            [activity("S02", "11:00", "11:20")], weather=weather,
            show_da_huy=cancellations,
        )
        self.assertTrue(replacement["hop_le"])
        self.assertFalse(any(slot["huy"] for slot in tools.tra_lich_show(SUNNY)))

    def test_draft_cannot_override_price_or_maintenance(self):
        closed_ride = {
            **activity("A09", "09:00", "09:45"),
            "maintenance": False,
            "gate_adult_vnd": 440_000,
        }
        lunch = {
            **activity("A07", "12:00", "12:40"),
            "extra_fee_adult_vnd": 0,
            "extra_fee_child_vnd": 0,
        }
        result = self.check([closed_ride, lunch], budget=2_420_000)
        self.assert_errors(result, "BAO_TRI", "VUOT_NGAN_SACH")
        self.assertEqual(result["tien_ve_cong"], 2_420_000)
        self.assertEqual(result["tong_tien"], 2_770_000)
        self.assertEqual(result["chi_tiet"][1]["tien"], 350_000)

    def test_rain_age_and_unknown_weather(self):
        self.assert_errors(self.check([activity("A08", "13:20", "14:05")], ages=[5],
                                      weather={"ngay": RAINY, "rain_from": None, "outdoor_ok": True}),
                           "GIOI_HAN_TUOI", "MUA_NGOAI_TROI")
        self.assert_errors(self.check([activity("A02", "13:00", "13:30")],
                                      weather={"ngay": SUNNY, "mua_tu": "13:15"}),
                           "MUA_NGOAI_TROI")
        self.assert_errors(self.check([activity("A02", "13:30", "14:00")],
                                      weather={"ngay": "2026-12-01"}),
                           "THIEU_THOI_TIET")
        self.assertTrue(self.check([activity("A02", "13:30", "14:00")],
                                    weather={"ngay": RAINY})["hop_le"])
        self.assertTrue(self.check([activity("A02", "17:30", "18:00")],
                                    weather={"ngay": RAINY})["hop_le"])

    def test_toddler_gate_price_and_minimum_budget(self):
        result = self.check([activity("A05", "10:00", "11:00")], budget=1_760_000, ages=[3])
        self.assertTrue(result["hop_le"])
        self.assertEqual(result["tong_tien"], 1_760_000)
        empty = self.check([], budget=2_400_000)
        self.assert_errors(empty, "LICH_TRONG", "VUOT_NGAN_SACH")
        self.assertEqual(empty["tien_ve_cong"], 2_420_000)

    def test_bad_input_and_missing_data_fail_closed(self):
        self.assert_errors(self.check([activity("A05", "11:00", "12:00")], ages=[]), "DAU_VAO_KHONG_HOP_LE")
        unknown = self.check([activity("khong_co", "11:00", "12:00")])
        self.assert_errors(unknown, "MUC_LICH_KHONG_HOP_LE")
        self.assertIsNone(unknown["tong_tien"])
        with TemporaryDirectory() as directory:
            with patch.object(tools, "PARK_DATA", Path(directory) / "missing.json"):
                self.assert_errors(self.check([activity("A05", "11:00", "12:00")]),
                                   "DU_LIEU_KHU_KHONG_HOP_LE")


if __name__ == "__main__":
    unittest.main()
