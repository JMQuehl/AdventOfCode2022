from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2022.tasks.task11.task11 import Task11
from advent_of_code_2022.advent_of_code_utils import parse_args


class Task11Tests(TaskTest, unittest.TestCase):
    task = Task11(parse_args([]))
    known_input = ["Monkey 0:\n",
                   "  Starting items: 79, 98\n",
                   "  Operation: new = old * 19\n",
                   "  Test: divisible by 23\n",
                   "    If true: throw to monkey 2\n",
                   "    If false: throw to monkey 3\n",
                   "\n",
                   "Monkey 1:\n",
                   "  Starting items: 54, 65, 75, 74\n",
                   "  Operation: new = old + 6\n",
                   "  Test: divisible by 19\n",
                   "    If true: throw to monkey 2\n",
                   "    If false: throw to monkey 0\n",
                   "\n",
                   "Monkey 2:\n",
                   "  Starting items: 79, 60, 97\n",
                   "  Operation: new = old * old\n",
                   "  Test: divisible by 13\n",
                   "    If true: throw to monkey 1\n",
                   "    If false: throw to monkey 3\n",
                   "\n",
                   "Monkey 3:\n",
                   "  Starting items: 74\n",
                   "  Operation: new = old + 3\n",
                   "  Test: divisible by 17\n",
                   "    If true: throw to monkey 0\n",
                   "    If false: throw to monkey 1"]
    known_output = 10605
    known_bonus_output = 2713310158
