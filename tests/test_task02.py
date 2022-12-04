from abstract_test import TaskTest
import unittest
from advent_of_code_2022.tasks.task02.task02 import Task02


class Task02Tests(TaskTest, unittest.TestCase):
    task = Task02()
    known_input = ["A Y\n", "B X\n", "C Z\n"]
    known_output = 15
    known_bonus_output = 12
