"""Kiểm hợp đồng giữa workflow lập lịch và công cụ của nhóm."""
import csv
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "codebase"))
import agent


class AgentToolsTest(unittest.TestCase):
    request = "1 người lớn, 0 trẻ, ngày 28/11/2026, 09:00–12:00, ngân sách 2 triệu"

    def test_fake_plan_uses_seeded_prices_and_names(self):
        with patch.object(agent, "MODEL_PROVIDER", "fake"), patch.object(
            agent, "call_model", return_value={"model": "fake", "text": ""}
        ):
            reply = agent.answer(self.request)["output"]
        self.assertIn("Lâu đài Kẹo Ngọt", reply)
        self.assertIn("Vé vào cổng: 880.000đ", reply)

    def test_invalid_hour_reaches_model_for_repair(self):
        def draft(start, end):
            item = {"diem_id": "A01", "bat_dau": start, "ket_thuc": end}
            return {"model": "test", "text": json.dumps({"lich_trinh": [item]})}

        with patch.object(agent, "MODEL_PROVIDER", "test"), patch.object(
            agent, "call_model", side_effect=[draft("13:00", "13:40"), draft("09:00", "09:40")]
        ) as model:
            reply = agent.answer(self.request)["output"]
        self.assertIn("NGOAI_GIO_CHUYEN_DI", model.call_args.args[1])
        self.assertIn("09:00–09:40", reply)
        self.assertNotIn("13:00–13:40", reply)

    def test_unavailable_date_stops_before_model(self):
        with patch.object(agent, "call_model") as model:
            reply = agent.answer(self.request.replace("28/11", "25/11"))["output"]
        model.assert_not_called()
        self.assertIn("2026-11-25", reply)

    def test_unauthorized_price_and_maintenance_change_stops_before_model(self):
        with (ROOT / "eval" / "benchmark.csv").open(encoding="utf-8-sig", newline="") as file:
            request = next(row["input"] for row in csv.DictReader(file) if row["id"] == "B15")
        with patch.object(agent, "call_model") as model:
            reply = agent.answer(request)["output"]

        model.assert_not_called()
        self.assertIn("từ chối", reply)
        self.assertIn("880.000đ", reply)
        self.assertIn("A09", reply)
        self.assertIn("bảo trì", reply)

    def test_midday_rain_sends_cancelled_show_back_for_repair(self):
        request = self.request.replace("12:00", "18:00") + ". Mưa từ 14:00."
        outdoor = {"diem_id": "S04", "bat_dau": "16:15", "ket_thuc": "16:45"}
        indoor = {"diem_id": "S03", "bat_dau": "15:00", "ket_thuc": "15:20"}
        replies = [
            {"model": "test", "text": json.dumps({"lich_trinh": [item]})}
            for item in (outdoor, indoor)
        ]
        with patch.object(agent, "MODEL_PROVIDER", "test"), patch.object(
            agent, "call_model", side_effect=replies
        ) as model:
            reply = agent.answer(request)["output"]

        self.assertEqual(model.call_count, 2)
        self.assertIn("SUAT_SHOW_KHONG_CO_HOAC_DA_HUY (S04)", model.call_args.args[1])
        self.assertIn("15:00–15:20", reply)
        self.assertNotIn("16:15–16:45", reply)
