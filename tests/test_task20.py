from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2022.tasks.task20.task20 import Task20
from advent_of_code_2022.advent_of_code_utils import parse_args


class Task20Tests(TaskTest, unittest.TestCase):
    task = Task20(parse_args(['--visualize']))
    known_input = ["1\n",
                   "2\n",
                   "-3\n",
                   "3\n",
                   "-2\n",
                   "0\n",
                   "4"]
    known_output = 3
    known_bonus_output = 0
