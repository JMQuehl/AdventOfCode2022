from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2022.tasks.task13.task13 import Task13
from advent_of_code_2022.advent_of_code_utils import parse_args


class Task13Tests(TaskTest, unittest.TestCase):
    task = Task13(parse_args(['--visualize']))
    known_input = ["[1,1,3,1,1]\n",
                   "[1,1,5,1,1]\n",
                   "\n",
                   "[[1],[2,3,4]]\n",
                   "[[1],4]\n",
                   "\n",
                   "[9]\n",
                   "[[8,7,6]]\n",
                   "\n",
                   "[[4,4],4,4]\n",
                   "[[4,4],4,4,4]\n",
                   "\n",
                   "[7,7,7,7]\n",
                   "[7,7,7]\n",
                   "\n",
                   "[]\n",
                   "[3]\n",
                   "\n",
                   "[[[]]]\n",
                   "[[]]\n",
                   "\n",
                   "[1,[2,[3,[4,[5,6,7]]]],8,9]\n",
                   "[1,[2,[3,[4,[5,6,0]]]],8,9]"]
    known_output = 13
    known_bonus_output = 140
