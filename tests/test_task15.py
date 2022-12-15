from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2022.tasks.task15.task15 import Task15
from advent_of_code_2022.advent_of_code_utils import parse_args


class Task05Tests(TaskTest, unittest.TestCase):
    task = Task15(parse_args(['--visualize']))
    known_input = ["Sensor at x=2, y=18: closest beacon is at x=-2, y=15\n",
                   "Sensor at x=9, y=16: closest beacon is at x=10, y=16\n",
                   "Sensor at x=13, y=2: closest beacon is at x=15, y=3\n",
                   "Sensor at x=12, y=14: closest beacon is at x=10, y=16\n",
                   "Sensor at x=10, y=20: closest beacon is at x=10, y=16\n",
                   "Sensor at x=14, y=17: closest beacon is at x=10, y=16\n",
                   "Sensor at x=8, y=7: closest beacon is at x=2, y=10\n",
                   "Sensor at x=2, y=0: closest beacon is at x=2, y=10\n",
                   "Sensor at x=0, y=11: closest beacon is at x=2, y=10\n",
                   "Sensor at x=20, y=14: closest beacon is at x=25, y=17\n",
                   "Sensor at x=17, y=20: closest beacon is at x=21, y=22\n",
                   "Sensor at x=16, y=7: closest beacon is at x=15, y=3\n",
                   "Sensor at x=14, y=3: closest beacon is at x=15, y=3\n",
                   "Sensor at x=20, y=1: closest beacon is at x=15, y=3"]
    known_output = 26
    known_bonus_output = 0
