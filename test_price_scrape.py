import unittest

from bookstore import parse_google_books_price


class TestParseGoogleBooksPrice(unittest.TestCase):
    def test_sale_info_list_price_amount(self):
        data = {
            "items": [
                {
                    "saleInfo": {
                        "listPrice": {"amount": 12.99},
                    },
                }
            ]
        }
        self.assertEqual(parse_google_books_price(data), "12.99")

    def test_sale_info_retail_price_amount(self):
        data = {
            "items": [
                {
                    "saleInfo": {
                        "retailPrice": {"amount": 9.99},
                    },
                }
            ]
        }
        self.assertEqual(parse_google_books_price(data), "9.99")

    def test_offers_amount_in_micros(self):
        data = {
            "items": [
                {
                    "saleInfo": {
                        "offers": [
                            {
                                "listPrice": {"amountInMicros": 15990000},
                            }
                        ]
                    },
                }
            ]
        }
        self.assertEqual(parse_google_books_price(data), "15.99")

    def test_volume_info_fallback(self):
        data = {
            "items": [
                {
                    "volumeInfo": {
                        "listPrice": {"amount": 8.5},
                    },
                }
            ]
        }
        self.assertEqual(parse_google_books_price(data), "8.50")

    def test_missing_price(self):
        self.assertIsNone(parse_google_books_price({"items": [{}]}))


if __name__ == "__main__":
    unittest.main()
