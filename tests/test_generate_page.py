import unittest
from src.generate_page import extract_title

class TestGeneratePage(unittest.TestCase):
    def test_extract_title_valid(self):
        title1 = extract_title("# hello")
        title2 = extract_title("# hello")
        title3 = extract_title("# hello#")
        title4 = extract_title("# .hello")
        title5 = extract_title("# #hello")

        self.assertEqual(title1, "hello")
        self.assertEqual(title2, "hello")
        self.assertEqual(title3, "hello#")
        self.assertEqual(title4, ".hello")
        self.assertEqual(title5, "#hello")

    def test_extract_title_invalid(self):
        with self.assertRaises(ValueError):
            extract_title("##hello")

        with self.assertRaises(ValueError):
            extract_title("#hello")

        with self.assertRaises(ValueError):
            extract_title("### Subtitle")
