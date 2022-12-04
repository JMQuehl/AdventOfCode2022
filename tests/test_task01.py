from abstract_test import TaskTest
import unittest
from advent_of_code_2022.tasks.task01.task01 import Task01


class Task01Tests(TaskTest, unittest.TestCase):
    task = Task01()
    known_input = ["1000\n",
                   "2000\n",
                   "3000\n",
                   "\n",
                   "4000\n",
                   "\n",
                   "5000\n",
                   "6000\n",
                   "\n",
                   "7000\n",
                   "8000\n",
                   "9000\n",
                   "\n",
                   "10000\n"]
    known_output = 24000
    known_bonus_output = 45000
