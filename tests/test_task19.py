from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2022.tasks.task18.task18 import Task18
from advent_of_code_2022.advent_of_code_utils import parse_args


class Task18Tests(TaskTest, unittest.TestCase):
    task = Task18(parse_args(['--visualize']))
    known_input = ["Blueprint 1:\n",
                   "  Each ore robot costs 4 ore.\n",
                   "  Each clay robot costs 2 ore.\n",
                   "  Each obsidian robot costs 3 ore and 14 clay.\n",
                   "  Each geode robot costs 2 ore and 7 obsidian.\n",
                   "\n",
                   "Blueprint 2:\n",
                   "  Each ore robot costs 2 ore.\n",
                   "  Each clay robot costs 3 ore.\n",
                   "  Each obsidian robot costs 3 ore and 8 clay.\n",
                   "  Each geode robot costs 3 ore and 12 obsidian."]
    known_output = 33
    known_bonus_output = 0
