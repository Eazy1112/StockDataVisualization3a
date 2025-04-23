import unittest
from datetime import datetime

def is_valid_symbol(symbol):
    return symbol.isalpha() and symbol.isupper() and 1 <= len(symbol) <= 7

def is_valid_chart_type(chart_type):
    return chart_type in ['1', '2']

def is_valid_time_series(time_series):
    return time_series in ['1', '2', '3', '4']

def is_valid_date_format(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

class TestStockVisualizerInputs(unittest.TestCase):

    def test_symbol_valid(self):
        self.assertTrue(is_valid_symbol("AAPL"))
        self.assertTrue(is_valid_symbol("GOOGL"))
        self.assertFalse(is_valid_symbol("aapl"))
        self.assertFalse(is_valid_symbol("AAPL123"))
        self.assertFalse(is_valid_symbol(""))

    def test_chart_type(self):
        self.assertTrue(is_valid_chart_type("1"))
        self.assertTrue(is_valid_chart_type("2"))
        self.assertFalse(is_valid_chart_type("3"))
        self.assertFalse(is_valid_chart_type(""))

    def test_time_series(self):
        self.assertTrue(is_valid_time_series("1"))
        self.assertTrue(is_valid_time_series("4"))
        self.assertFalse(is_valid_time_series("5"))
        self.assertFalse(is_valid_time_series("0"))

    def test_start_date_format(self):
        self.assertTrue(is_valid_date_format("2024-01-01"))
        self.assertFalse(is_valid_date_format("01-01-2024"))
        self.assertFalse(is_valid_date_format("2024/01/01"))
        self.assertFalse(is_valid_date_format("2024-13-01"))

    def test_end_date_format(self):
        self.assertTrue(is_valid_date_format("2024-12-31"))
        self.assertFalse(is_valid_date_format("12-31-2024"))
        self.assertFalse(is_valid_date_format("invalid-date"))
        self.assertFalse(is_valid_date_format(""))

if __name__ == '__main__':
    unittest.main()
