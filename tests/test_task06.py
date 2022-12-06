from tests.abstract_test import TaskTest
import unittest
from advent_of_code_2022.tasks.task06.task06 import Task06
import sys


class Task06Tests(TaskTest, unittest.TestCase):
    task = Task06()
    known_input = ["mjqjpqmgbljsphdztnvjfqwrcgsmlb",
                   "bvwbjplbgvbhsrlpgdmjqwftvncz",
                   "nppdvjthqldpwncqszvftbrmjlhg",
                   "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
                   "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"]
    known_output = [7, 5, 6, 10, 11]
    known_bonus_output = [19, 23, 23, 29, 26]

    def test_given_example(self):
        for i in range(len(self.known_input)):
            assert self.task.solve_task([self.known_input[i]]) == self.known_output[i]

    def test_given_bonus_example(self):
        for i in range(len(self.known_input)):
            assert self.task.solve_bonus_task([self.known_input[i]]) == self.known_bonus_output[i]

    def test_input_validation(self):
        for line in self.known_input:
            assert self.task.is_input_valid([line])
