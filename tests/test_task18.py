from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2022.tasks.task18.task18 import Task18
from advent_of_code_2022.advent_of_code_utils import parse_args


class Task18Tests(TaskTest, unittest.TestCase):
    task = Task18(parse_args(['--visualize']))
    known_input = ["2,2,2\n",
                   "1,2,2\n",
                   "3,2,2\n",
                   "2,1,2\n",
                   "2,3,2\n",
                   "2,2,1\n",
                   "2,2,3\n",
                   "2,2,4\n",
                   "2,2,6\n",
                   "1,2,5\n",
                   "3,2,5\n",
                   "2,1,5\n",
                   "2,3,5"]
    known_output = 64
    known_bonus_output = 58
