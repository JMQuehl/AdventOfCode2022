from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2022.tasks.task15.task15 import Task15
from advent_of_code_2022.advent_of_code_utils import parse_args


class Task15Tests(TaskTest, unittest.TestCase):
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

    def test_given_example(self):
        self.task.parse_input(self.known_input)
        assert sum([x[1] - x[0] + 1 for x in self.task.get_impossible_positions(10)])

    def test_given_bonus_example(self):
        self.task.parse_input(self.known_input)
        position = self.task.find_possible_position_in_range(20)
        assert (position[0] * 4000000) + position[1] == 56000011
