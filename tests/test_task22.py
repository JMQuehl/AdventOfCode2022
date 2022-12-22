from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2022.tasks.task22.task22 import Task22
from advent_of_code_2022.advent_of_code_utils import parse_args


class Task22Tests(TaskTest, unittest.TestCase):
    task = Task22(parse_args(['--visualize']))
    known_input = ["        ...#    \n",
                   "        .#..    \n",
                   "        #...    \n",
                   "        ....    \n",
                   "...#.......#    \n",
                   "........#...    \n",
                   "..#....#....    \n",
                   "..........#.    \n",
                   "        ...#....\n",
                   "        .....#..\n",
                   "        .#......\n",
                   "        ......#.\n",
                   "\n",
                   "10R5L5R10L4R5L5"]
    known_output = 6032
    known_bonus_output = 5031
