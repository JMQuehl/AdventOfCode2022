from advent_of_code_2022.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List, Tuple, Dict
import re


class Monkey:
    waiting_for: Tuple[str, str]
    number: str
    operation: str
    number_monkey: bool

    def __init__(self, monkey_string: str):
        nums = re.findall("\d+", monkey_string)
        if nums:
            self.number = nums[0]
            self.number_monkey = True
        else:
            self.number = -1
            split_string = monkey_string.split()
            self.operation = split_string[-2]
            self.waiting_for = (split_string[-3], split_string[-1])
            self.number_monkey = False

    def yell(self, monkey_map: Dict[str, 'Monkey']) -> int:
        if self.number_monkey:
            return int(self.number)
        else:
            num1 = monkey_map[self.waiting_for[0]].yell(monkey_map)
            num2 = monkey_map[self.waiting_for[1]].yell(monkey_map)
            assert self.operation in '+-*/=='
            return eval('num1 ' + self.operation + ' num2')

    def give_equation(self, monkey_map: Dict[str, 'Monkey']) -> str:
        if self.number_monkey:
            return self.number
        else:
            return monkey_map[self.waiting_for[0]].give_equation(monkey_map) + ' ' + self.operation + ' ' + monkey_map[
                self.waiting_for[1]].give_equation(monkey_map)


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
        you.number = 'x'
        print(root.give_equation(self.monkey_map))

        return 0
        flip = False
        yell = root.yell(self.monkey_map)
        while not yell:
            print('root yelled: %s, checking number: %d' % (yell, you.number))
            if not flip:
                you.number = -you.number + 1
                flip = True
            else:
                you.number = -you.number
                flip = False
            yell = root.yell(self.monkey_map)
        return you.number

    def is_input_valid(self, input_file_content: List[str]):
        return all(
            re.fullmatch("[a-z]{4}: ((\d+)|([a-z]{4} [+\-*/] [a-z]{4}))\n?", line) for line in input_file_content)
