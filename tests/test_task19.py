from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2022.tasks.task19.task19 import Task19
from advent_of_code_2022.advent_of_code_utils import parse_args


class Task19Tests(TaskTest, unittest.TestCase):
    task = Task19(parse_args(['--visualize']))
    known_input = ["Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.\n",
                   "Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."]
    known_output = 33
    known_bonus_output = 56*62
