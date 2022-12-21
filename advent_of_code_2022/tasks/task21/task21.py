from advent_of_code_2022.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List, Tuple, Dict
import re
from sympy import Eq, solve, Symbol


class Monkey:
    waiting_for: Tuple[str, str]
    operation: str
    number_monkey: bool

    def __init__(self, monkey_string: str):
        nums = re.findall("\d+", monkey_string)
        if nums:
            self.number = int(nums[0])
            self.number_monkey = True
        else:
            split_string = monkey_string.split()
            self.operation = split_string[-2]
            self.waiting_for = (split_string[-3], split_string[-1])
            self.number_monkey = False

    def yell(self, monkey_map: Dict[str, 'Monkey']) -> int:
        if self.number_monkey:
            return self.number  # in part 2 this might be a sympy symbol and not a number
        elif self.operation in '+-*/':
            num1 = monkey_map[self.waiting_for[0]].yell(monkey_map)
            num2 = monkey_map[self.waiting_for[1]].yell(monkey_map)
            return eval('num1 ' + self.operation + ' num2')
        elif self.operation == '==':
            num1 = monkey_map[self.waiting_for[0]].yell(monkey_map)
            num2 = monkey_map[self.waiting_for[1]].yell(monkey_map)
            return solve(Eq(num1, num2))  # sympy is used for solving the equation.


class Task21(AdventOfCodeProblem):
    monkey_map: Dict[str, Monkey]

    def __init__(self, args):
        super().__init__(args)
        self.answer_text = 'Root monkey will yell: %d.'
        self.bonus_answer_text = 'In order for the root monkey to have two equal numbers, you have to yell: %d.'
        self.task_number = 21

    def parse_input(self, input_file_content: List[str]):
        self.monkey_map = dict()
        for line in input_file_content:
            self.monkey_map[line[:4]] = Monkey(line)

    def solve_task(self, input_file_content: List[str]):
        self.parse_input(input_file_content)
        root = self.monkey_map['root']
        return root.yell(self.monkey_map)

    def solve_bonus_task(self, input_file_content: List[str]):
        self.parse_input(input_file_content)
        you = self.monkey_map['humn']
        root = self.monkey_map['root']
        root.operation = '=='
        you.number = Symbol('x')
        solution = int(root.yell(self.monkey_map)[0])
        return solution

    def is_input_valid(self, input_file_content: List[str]):
        return all(
            re.fullmatch("[a-z]{4}: ((\d+)|([a-z]{4} [+\-*/] [a-z]{4}))\n?", line) for line in input_file_content)
