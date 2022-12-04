import unittest
from advent_of_code_2022.tasks.task01.task01 import Task01


class MainTaskTests(unittest.TestCase):

    def test_given_example(self):
        task = Task01()
        input_lines = ["1000\n",
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
        assert task.solve_task(input_lines) == 24000
