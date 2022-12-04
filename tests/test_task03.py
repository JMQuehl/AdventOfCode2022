import string
from abstract_test import TaskTest
import unittest
from advent_of_code_2022.tasks.task03.task03 import Task03, get_letter_value


class Task03Tests(TaskTest, unittest.TestCase):
    task = Task03()
    known_input = ["vJrwpWtwJgWrhcsFMMfFFhFp\n",
                   "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n",
                   "PmmdzqPrVvPwwTWBwg\n",
                   "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n",
                   "ttgJtRGJQctTZtZT\n",
                   "CrZsJsPPZsGzwwsLwLmpwMDw"]
    known_output = 157
    known_bonus_output = 70

    def test_letter_value(self):
        expected_result = list(range(1, 52 + 1))
        input_list = string.ascii_lowercase + string.ascii_uppercase
        result = [get_letter_value(x) for x in input_list]
        assert result == expected_result

