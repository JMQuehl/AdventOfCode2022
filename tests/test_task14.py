from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2022.tasks.task14.task14 import Task14
from advent_of_code_2022.advent_of_code_utils import parse_args


class Task05Tests(TaskTest, unittest.TestCase):
    task = Task14(parse_args(['--visualize']))
    known_input = ["498,4 -> 498,6 -> 496,6\n",
                   "503,4 -> 502,4 -> 502,9 -> 494,9"]
    known_output = 24
    known_bonus_output = 93
