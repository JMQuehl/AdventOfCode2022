from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2022.tasks.task17.task17 import Task17
from advent_of_code_2022.advent_of_code_utils import parse_args


class Task17Tests(TaskTest, unittest.TestCase):
    task = Task17(parse_args(['--visualize']))
    known_input = [">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"]
    known_output = 3068
    known_bonus_output = 1514285714288

    def test_given_bonus_example(self):
        second_instance = Task17(parse_args(['--visualize']))
        assert second_instance.solve_bonus_task(self.known_input) == self.known_bonus_output
