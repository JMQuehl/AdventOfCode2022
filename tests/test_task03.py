import string
import unittest
from advent_of_code_2022.tasks.task03.task03 import Task03, get_letter_value


class MainTaskTests(unittest.TestCase):
    task = Task03()
    known_input = ["vJrwpWtwJgWrhcsFMMfFFhFp\n",
                   "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n",
                   "PmmdzqPrVvPwwTWBwg\n",
                   "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n",
                   "ttgJtRGJQctTZtZT\n",
                   "CrZsJsPPZsGzwwsLwLmpwMDw\n"]

    def test_given_example(self):
        assert self.task.solve_task(self.known_input) == 157

    def test_letter_value(self):
        expected_result = list(range(1, 52 + 1))
        input_list = string.ascii_lowercase + string.ascii_uppercase
        result = [get_letter_value(x) for x in input_list]
        assert result == expected_result

