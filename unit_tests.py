import unittest
from utils import wedding_func


class TestGraph(unittest.TestCase):

    def setUp(self) -> None:
        """

         graphs initialising

        """
        self.first_list = [(1, 2), (2, 4), (3, 5)]
        self.second_list = [(1, 2), (2, 4), (1, 3), (7, 5), (8, 10)]
        self.third_list = [(1, 2)]
        self.forth_list = []
        self.fifth_list = [(1, 2), (2, 4), (4, 6), (6, 7)]
        self.sixth_list = [(1, 2), (3, 4), (5, 6)]
        self.seventh_list = [[(1, 2), (2, 4), (1, 3), (3, 5), (8, 10)]]

        self.seventh_list_lenght = 1200

        """

        Initialising results

        """
        self.first_result = 4
        self.second_result = 12
        self.third_result = 0
        self.forth_result = 0
        self.fifth_result = 0
        self.sixth_result = 6
        self.seventh_result = 0
        """

        Directly, Tests

        """
    def test_first_list_from_example(self):
        self.assertEqual(wedding_func(self.first_list, len(self.first_list)),
                         self.first_result)

    def test_second_list_from_example(self):
        self.assertEqual(wedding_func(self.second_list, len(self.second_list)),
                         self.second_result)

    def test_third_list_from_example(self):
        self.assertEqual(wedding_func(self.third_list, len(self.third_list)),
                         self.third_result)

    def test_forth_list_from_example(self):
        self.assertEqual(wedding_func(self.forth_list, len(self.forth_list)),
                         self.forth_result)

    def test_fifth_list_from_example(self):
        self.assertEqual(wedding_func(self.fifth_list, len(self.fifth_list)),
                         self.fifth_result)

    def test_sixth_list_from_example(self):
        self.assertEqual(wedding_func(self.sixth_list, len(self.sixth_list)),
                         self.sixth_result)

    def test_seventh_list_from_example(self):
        self.assertEqual(wedding_func(self.seventh_list, self.seventh_list_lenght),
                         self.seventh_result)


if __name__ == '__main__':
    unittest.main()