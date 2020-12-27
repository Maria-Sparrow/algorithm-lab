import unittest

from main import naive_search


class MyTestCase(unittest.TestCase):
    def test_naive_search(self):
        self.assertEqual(naive_search("aabaacaadaabaaba", "aaba"), [(0, 4), (9, 13), (12, 16)])
        self.assertEqual(naive_search("AABCCAADDEE", "FAA"), [])
        self.assertEqual(naive_search("AAAAAAA", "AAAA"), [(0, 4), (1, 5), (2, 6), (3, 7)])
        self.assertEqual(naive_search("AAAAAAAAAAAAAAAAAB", "AAAB"), [(14, 18)])


if __name__ == '__main__':
    unittest.main()
