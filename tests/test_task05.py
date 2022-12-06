from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2022.tasks.task05.task05 import Task05


class Task05Tests(TaskTest, unittest.TestCase):
    task = Task05()
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
