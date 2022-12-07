from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2022.tasks.task05.task05 import Task05
from advent_of_code_2022.advent_of_code_utils import parse_args


class Task05Tests(TaskTest, unittest.TestCase):
    task = Task05(parse_args([]))
    known_input = ["    [D]    \n",
                   "[N] [C]    \n",
                   "[Z] [M] [P]\n",
                   " 1   2   3 \n",
                   "\n",
                   "move 1 from 2 to 1\n",
                   "move 3 from 1 to 3\n",
                   "move 2 from 2 to 1\n",
                   "move 1 from 1 to 2"]
    known_output = "CMZ"
    known_bonus_output = "MCD"
