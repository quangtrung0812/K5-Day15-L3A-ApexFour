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

    def test_b17_b21_time_parser_and_b25_out_of_scope_guardrail(self):
        with (ROOT / "eval" / "benchmark.csv").open(encoding="utf-8-sig", newline="") as file:
            by_id = {row["id"]: row["input"] for row in csv.DictReader(file)}

        with patch.object(agent, "MODEL_PROVIDER", "fake"), patch.object(
            agent, "call_model", return_value={"model": "fake", "text": ""}
        ):
            r_b17 = agent.answer(by_id["B17"])["output"]
            r_b21 = agent.answer(by_id["B21"])["output"]
        self.assertIn("LỊCH TRÌNH ĐỀ XUẤT", r_b17)
        self.assertNotIn("[A13]", r_b17)
        self.assertIn("LỊCH TRÌNH ĐỀ XUẤT", r_b21)
        self.assertNotIn("[A02]", r_b21)

        with patch.object(agent, "call_model") as model:
            r_b25 = agent.answer(by_id["B25"])["output"]
        model.assert_not_called()
        self.assertIn("từ chối", r_b25.lower())

    def test_ai_py_gemini_and_openai_usage_parsing(self):
        import ai

        gemini_payload = {
            "candidates": [{"content": {"parts": [{"text": "{\"lich_trinh\": []}"}]}}],
            "usageMetadata": {"promptTokenCount": 310, "candidatesTokenCount": 85, "thoughtsTokenCount": 15},
        }
        with patch.object(ai, "MODEL_PROVIDER", "gemini"), patch.object(
            ai, "MODEL_NAME", "gemini-2.5-flash"
        ), patch.object(ai, "API_KEY", "dummy-key"), patch.object(
            ai, "post_json", return_value=gemini_payload
        ):
            res_g = ai.call_model("sys", "usr")
        self.assertEqual(res_g["model"], "gemini-2.5-flash")
        self.assertEqual(res_g["tokens_in"], 310)
        self.assertEqual(res_g["tokens_out"], 100)

        openai_payload = {
            "choices": [{"message": {"content": "{\"lich_trinh\": []}"}}],
            "usage": {"prompt_tokens": 200, "completion_tokens": 60},
        }
        with patch.object(ai, "MODEL_PROVIDER", "openai"), patch.object(
            ai, "MODEL_NAME", "gpt-4o-mini"
        ), patch.object(ai, "API_KEY", "dummy-key"), patch.object(
            ai, "post_json", return_value=openai_payload
        ):
            res_o = ai.call_model("sys", "usr")
        self.assertEqual(res_o["model"], "gpt-4o-mini")
        self.assertEqual(res_o["tokens_in"], 200)
        self.assertEqual(res_o["tokens_out"], 60)

    def test_b14_age_injection_cites_limits_and_safe_rides(self):
        with (ROOT / "eval" / "benchmark.csv").open(encoding="utf-8-sig", newline="") as file:
            b14 = next(row["input"] for row in csv.DictReader(file) if row["id"] == "B14")
        with patch.object(agent, "call_model") as model:
            reply = agent.answer(b14)["output"]
        model.assert_not_called()
        self.assertIn("từ chối", reply.lower())
        self.assertIn("A08", reply)
        self.assertIn("A10", reply)
        self.assertNotIn("A04", reply)
        self.assertIn("A01", reply)

    def test_b22_unavailable_date_suggests_available_dates(self):
        with (ROOT / "eval" / "benchmark.csv").open(encoding="utf-8-sig", newline="") as file:
            b22 = next(row["input"] for row in csv.DictReader(file) if row["id"] == "B22")
        with patch.object(agent, "call_model") as model:
            reply = agent.answer(b22)["output"]
        model.assert_not_called()
        self.assertIn("2026-12-05", reply)
        self.assertIn("2026-11-28", reply)
        self.assertIn("2026-11-30", reply)


if __name__ == "__main__":
    unittest.main()
