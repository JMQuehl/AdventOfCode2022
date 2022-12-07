from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2022.tasks.task07.task07 import Task07
from advent_of_code_2022.advent_of_code_utils import parse_args


class Task07Tests(TaskTest, unittest.TestCase):
    task = Task07(parse_args([]))
    known_input = ["$ cd /\n",
                   "$ ls\n",
                   "dir a\n",
                   "14848514 b.txt\n",
                   "8504156 c.dat\n",
                   "dir d\n",
                   "$ cd a\n",
                   "$ ls\n",
                   "dir e\n",
                   "29116 f\n",
                   "2557 g\n",
                   "62596 h.lst\n",
                   "$ cd e\n",
                   "$ ls\n",
                   "584 i\n",
                   "$ cd ..\n",
                   "$ cd ..\n",
                   "$ cd d\n",
                   "$ ls\n",
                   "4060174 j\n",
                   "8033020 d.log\n",
                   "5626152 d.ext\n",
                   "7214296 k"]

    known_output = 95437
    known_bonus_output = 24933642
