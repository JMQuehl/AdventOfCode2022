import unittest
from advent_of_code_2022.tasks.task02.task02 import Task02


class MainTaskTests(unittest.TestCase):
    task = Task02()
    known_input = ["A Y\n", "B X\n", "C Z\n"]

    def test_given_example(self):
        assert self.task.solve_task(self.known_input) == 15

    def test_given_bonus_example(self):
        assert self.task.solve_bonus_task(self.known_input) == 12
