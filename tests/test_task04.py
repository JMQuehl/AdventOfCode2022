from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2022.tasks.task04.task04 import Task04


class Task04Tests(TaskTest, unittest.TestCase):
    task = Task04()
    known_input = ["2-4,6-8\n",
                   "2-3,4-5\n",
                   "5-7,7-9\n",
                   "2-8,3-7\n",
                   "6-6,4-6\n",
                   "2-6,4-8"]
    known_output = 2
    known_bonus_output = 4
