import unittest
from advent_of_code_2022.tasks.task02.task02 import Task02


class MainTaskTests(unittest.TestCase):

    def test_given_example(self):
        task = Task02()
        input_lines = ["A Y", "B X", "C Z"]
        assert task.solve_task(input_lines) == 15
