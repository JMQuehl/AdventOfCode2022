from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2022.tasks.task08.task08 import Task08
from advent_of_code_2022.advent_of_code_utils import parse_args


class Task08Tests(TaskTest, unittest.TestCase):
    task = Task08(parse_args([]))
    known_input = ["30373\n",
                   "25512\n",
                   "65332\n",
                   "33549\n",
                   "35390"]

    known_output = 21
    known_bonus_output = 8

    def test_calc_scenic_score(self):
        self.task.parse_input(self.known_input)
        for i in range(len(self.known_input)):
            assert self.task.calc_scenic_score((i, 0)) == 0
            assert self.task.calc_scenic_score((i, len(self.known_input[0].replace('\n', '')) - 1)) == 0
        for j in range(len(self.known_input[0].replace('\n', ''))):
            assert self.task.calc_scenic_score((0, j)) == 0
            assert self.task.calc_scenic_score((len(self.known_input) - 1, j)) == 0
        assert self.task.calc_scenic_score((1, 2)) == 4
        assert self.task.calc_scenic_score((3, 2))
