import unittest
from advent_of_code_2022.tasks.task01.task01 import Task01


class MainTaskTests(unittest.TestCase):
    task = Task01()
    known_input = ["1000\n",
                   "2000\n",
                   "3000\n",
                   "\n",
                   "4000\n",
                   "\n",
                   "5000\n",
                   "6000\n",
                   "\n",
                   "7000\n",
                   "8000\n",
                   "9000\n",
                   "\n",
                   "10000\n"]

    def test_given_example(self):
        assert self.task.solve_task(self.known_input) == 24000

    def test_given_bonus_example(self):
        assert self.task.solve_bonus_task(self.known_input) == 4500
