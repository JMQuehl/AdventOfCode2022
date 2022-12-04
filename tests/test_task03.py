import unittest
from advent_of_code_2022.tasks.task03.task03 import Task03


class MainTaskTests(unittest.TestCase):
    task = Task03()
    known_input = ["vJrwpWtwJgWrhcsFMMfFFhFp\n",
                   "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n",
                   "PmmdzqPrVvPwwTWBwg\n",
                   "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n",
                   "ttgJtRGJQctTZtZT\n",
                   "CrZsJsPPZsGzwwsLwLmpwMDw\n"]

    def test_given_example(self):
        assert self.task.solve_task(self.input_lines) == 157
