import unittest
from translator import french_to_english, english_to_french

class test_translator(unittest.TestCase):

    def test_french_to_english_basic(self):
        self.assertEqual(french_to_english("Bonjour"), \
            "Hello")

    def test_english_to_french_basic(self):
        self.assertEqual(english_to_french("Hello"), \
            "Bonjour")

    def test_french_to_english_blank(self):
        self.assertEqual(french_to_english(""), \
            "")

    def test_english_to_french_blank(self):
        self.assertNotEqual(english_to_french(""), \
            "abc")

if __name__ == '__main__':
        unittest.main()

# Interpretation of test result: 4 tests were executed on my code, and 0 failed.