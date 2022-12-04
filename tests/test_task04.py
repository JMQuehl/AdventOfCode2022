import string
import unittest
from advent_of_code_2022.tasks.task04.task04 import Task04


class MainTaskTests(unittest.TestCase):
    task = Task04()
    known_input = ["2-4,6-8\n",
                   "2-3,4-5\n",
                   "5-7,7-9\n",
                   "2-8,3-7\n",
                   "6-6,4-6\n",
                   "2-6,4-8"]

    def test_given_example(self):
        assert self.task.solve_task(self.known_input) == 157

    def test_letter_value(self):
        expected_result = list(range(1, 52 + 1))
        input_list = string.ascii_lowercase + string.ascii_uppercase
        result = [get_letter_value(x) for x in input_list]
        assert result == expected_result
