import unittest

from ijones_algo import find_ways


class SuccessfulWaysTest(unittest.TestCase):
    def \
            test_find_successful_ways_1(self):
        corridor = [["a", "a", "a"], ["c", "a", "b"], ["d", "e", "f"]]
        successful_ways_number = find_ways(corridor, 3, 3)
        self.assertEqual(5, successful_ways_number)

    def test_find_successful_ways_2(self):
        corridor = [["a", "b", "c", "d", "e", "f", "a", "g", "h", "i"]]
        successful_ways_number = find_ways(corridor, 10, 1)
        self.assertEqual(2, successful_ways_number)

    def test_find_successful_ways_3(self):
        corridor = [["a", "a", "a", "a", "a", "a", "a"], ["a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a"], ["a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a"], ["a", "a", "a", "a", "a", "a", "a"]]
        successful_ways_number = find_ways(corridor, 7, 6)
        self.assertEqual(201684, successful_ways_number)

    def test_find_successful_ways_4(self):
        corridor = [["a"]]
        successful_ways_number = find_ways(corridor, 1, 1)
        self.assertEqual(1, successful_ways_number)


if __name__ == '__main__':
    unittest.main()
