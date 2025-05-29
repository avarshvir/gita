# test/test_gita.py

import unittest
from gita.utils import (
    get_summary,
    get_verse,
    get_all_verses,
    list_available_summaries,
    is_valid_chapter,
    is_valid_verse,
    get_chapter_title
)

class TestGita(unittest.TestCase):

    def test_get_summary(self):
        result = get_summary(1)
        self.assertTrue(len(result) > 50)  
        self.assertIn("arjuna", result.lower())

    def test_get_verse(self):
        self.assertTrue(isinstance(get_verse(1, 1.1), str))

    def test_is_valid_chapter(self):
        self.assertTrue(is_valid_chapter(1))
        self.assertFalse(is_valid_chapter(20))

    def test_is_valid_verse(self):
        self.assertTrue(is_valid_verse(1, 1.1))
        self.assertFalse(is_valid_verse(1, 999))

    def test_chapter_title(self):
        self.assertEqual(get_chapter_title(1), "Arjuna Vishada Yoga - The Yoga of Arjuna's Dejection")
        self.assertIn("Chapter", get_chapter_title(99))

    def test_list_available_summaries(self):
        self.assertIn(1, list_available_summaries())

if __name__ == '__main__':
    unittest.main()
