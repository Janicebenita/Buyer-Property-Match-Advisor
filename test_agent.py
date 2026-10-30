import unittest
from agent import match_property


class MatchTests(unittest.TestCase):
    def test_trade_off_is_visible(self):
        result = match_property({"max_price": 100, "min_bedrooms": 2}, {"id": "L1", "price": 120, "bedrooms": 2})
        self.assertIn("budget", result["trade_offs"])
        self.assertTrue(result["human_review_required"])


if __name__ == "__main__":
    unittest.main()
