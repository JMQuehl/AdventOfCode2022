from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2022.tasks.task21.task21 import Task21
from advent_of_code_2022.advent_of_code_utils import parse_args


class Task19Tests(TaskTest, unittest.TestCase):
    task = Task21(parse_args(['--visualize']))
    known_input = ["root: pppw + sjmn\n",
                   "dbpl: 5\n",
                   "cczh: sllz + lgvd\n",
                   "zczc: 2\n",
                   "ptdq: humn - dvpt\n",
                   "dvpt: 3\n",
                   "lfqf: 4\n",
                   "humn: 5\n",
                   "ljgn: 2\n",
                   "sjmn: drzm * dbpl\n",
                   "sllz: 4\n",
                   "pppw: cczh / lfqf\n",
                   "lgvd: ljgn * ptdq\n",
                   "drzm: hmdt - zczc\n",
                   "hmdt: 32"]
    known_output = 152
    known_bonus_output = 301
