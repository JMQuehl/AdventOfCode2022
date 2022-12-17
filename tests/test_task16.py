from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2022.tasks.task16.task16 import Task16
from advent_of_code_2022.advent_of_code_utils import parse_args


class Task16Tests(TaskTest, unittest.TestCase):
    task = Task16(parse_args(['--visualize']))
    known_input = ["Valve AA has flow rate=0; tunnels lead to valves DD, II, BB\n",
                   "Valve BB has flow rate=13; tunnels lead to valves CC, AA\n",
                   "Valve CC has flow rate=2; tunnels lead to valves DD, BB\n",
                   "Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE\n",
                   "Valve EE has flow rate=3; tunnels lead to valves FF, DD\n",
                   "Valve FF has flow rate=0; tunnels lead to valves EE, GG\n",
                   "Valve GG has flow rate=0; tunnels lead to valves FF, HH\n",
                   "Valve HH has flow rate=22; tunnel leads to valve GG\n",
                   "Valve II has flow rate=0; tunnels lead to valves AA, JJ\n",
                   "Valve JJ has flow rate=21; tunnel leads to valve II"]
    known_output = 1651
    known_bonus_output = 1707
