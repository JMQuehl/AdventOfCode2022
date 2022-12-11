import functools
import operator

from advent_of_code_2022.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List, Tuple
import re
from collections import deque
from operator import mul
from functools import reduce


class Monkey:
    items: deque[int]
    operator_spec: List[str]
    divisibility_check_number: int
    target_monkeys: List[int]

    def __init__(self, string_input: List[str]):
        self.items = deque([int(x.replace(',', '')) for x in string_input[1].split()[2:]])
        self.operator_spec = string_input[2].split()[-2:]
        self.divisibility_check_number = int(string_input[3].split()[-1])
        self.target_monkeys = [int(string_input[4].split()[-1])]
        self.target_monkeys.append(int(string_input[5].split()[-1]))

    def _apply_operation(self, old: int) -> int:
        second_term = old if self.operator_spec[1] == 'old' else int(self.operator_spec[1])
        return old + second_term if self.operator_spec[0] == '+' else old * second_term

    def take_turn(self, monkey_list: List['Monkey'], feel_relief: bool, common_multiple: int) -> int:
        number_of_inspections = len(self.items)
        while self.items:
            new_score = self._apply_operation(self.items.popleft()) // 3 if feel_relief else self._apply_operation(
                self.items.popleft())
            if new_score % self.divisibility_check_number == 0:
                monkey_list[self.target_monkeys[0]].items.append(new_score % common_multiple)
            else:
                monkey_list[self.target_monkeys[1]].items.append(new_score % common_multiple)
        return number_of_inspections


class Task11(AdventOfCodeProblem):
    valid_res = ["Monkey \d+:\n?", "  Starting items: (\d+, )*\d+\n?", "  Operation: new = old [*+] (old|\d+)\n?",
                 "  Test: divisible by \d+\n?", "    If true: throw to monkey \d+\n?",
                 "    If false: throw to monkey \d+\n?", "\n?"]

    def __init__(self, args):
        super().__init__(args)
        self.answer_text = "The level of monkey business is: %d"
        self.bonus_answer_text = "After 10000 rounds and without relief the level of monkey business is %d"
        self.task_number = 11

    def _calc_monkey_business(self, input_file_content: List[str], feel_relief: bool, number_of_rounds: int) -> int:
        split_input = [input_file_content[i:i + 7] for i in range(0, len(input_file_content), 7)]
        monkeys = [Monkey(x) for x in split_input]
        monkey_activity = [0] * len(monkeys)
        common_multiple = functools.reduce(operator.mul, [x.divisibility_check_number for x in monkeys])
        for i in range(number_of_rounds):  # number of rounds
            for j in range(len(monkeys)):
                monkey_activity[j] += monkeys[j].take_turn(monkeys, feel_relief, common_multiple)
        monkey_activity.sort()
        return monkey_activity[-1] * monkey_activity[-2]

    def solve_task(self, input_file_content: List[str]):
        return self._calc_monkey_business(input_file_content, True, 20)

    def solve_bonus_task(self, input_file_content: List[str]):
        return self._calc_monkey_business(input_file_content, False, 10000)

    def is_input_valid(self, input_file_content: List[str]):
        return all([any([re.fullmatch(x, line) for x in self.valid_res]) for line in input_file_content])
        # not tested if the order of lines is ok.
