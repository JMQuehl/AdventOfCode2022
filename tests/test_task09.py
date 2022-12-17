from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2022.tasks.task09.task09 import Task09
from advent_of_code_2022.advent_of_code_utils import parse_args


class Task09Tests(TaskTest, unittest.TestCase):
    task = Task09(parse_args(["--visualize"]))
    known_input = ["R 4\n",
                   "U 4\n",
                   "L 3\n",
                   "D 1\n",
                   "R 4\n",
                   "D 1\n",
                   "L 5\n",
                   "R 2"]
    known_bonus_input = ["R 5\n",
                         "U 8\n",
                         "L 8\n",
                         "D 3\n",
                         "R 17\n",
                         "D 10\n",
                         "L 25\n",
                         "U 20"]
    known_output = 13
    known_bonus_output = [1, 36]

    def test_given_bonus_example(self):
        assert self.task.solve_bonus_task(self.known_input) == self.known_bonus_output[0]
        assert self.task.solve_bonus_task(self.known_bonus_input) == self.known_bonus_output[1]
