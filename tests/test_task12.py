from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2022.tasks.task12.task12 import Task12
from advent_of_code_2022.advent_of_code_utils import parse_args


class Task12Tests(TaskTest, unittest.TestCase):
    task = Task12(parse_args(['--visualize']))
    known_input = ["Sabqponm\n",
                   "abcryxxl\n",
                   "accszExk\n",
                   "acctuvwj\n",
                   "abdefghi"]
    known_output = 31
    known_bonus_output = 29
