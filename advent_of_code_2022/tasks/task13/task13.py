import functools
import json
import re

from advent_of_code_2022.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List


def parse_input(input_file_content: List[str]) -> List:
    input_without_empty_lines = [x.replace('\n', '') for x in input_file_content if x != '\n']
    return [json.loads(x) for x in input_without_empty_lines]


def compare_lists(left, right) -> int:
    for i in range(min(len(left), len(right))):
        if type(left[i]) == int and type(right[i]) == int:
            if left[i] != right[i]:
                return left[i] - right[i]
        elif type(left[i]) == list:
            if type(right[i]) == list:  # both values are lists -> recursion
                smaller = compare_lists(left[i], right[i])
                if smaller != 0: return smaller
            else:  # left is a list, right is a list of numbers
                smaller = compare_lists(left[i], [right[i]])
                if smaller != 0: return smaller
        else:  # right is a list, left is a list of numbers
            smaller = compare_lists([left[i]], right[i])
            if smaller != 0: return smaller
    if len(left) != len(right):
        return len(left) - len(right)
    return 0


class Task13(AdventOfCodeProblem):

    def __init__(self, args):
        super().__init__(args)
        self.answer_text = "The sum of indexes that are in the right order is: %d"
        self.bonus_answer_text = "The decoder key for the distress signal is: %d"
        self.task_number = 13

    def solve_task(self, input_file_content: List[str]):
        parsed_lines = parse_input(input_file_content)
        nested_lists = [parsed_lines[i:i + 2] for i in range(0, len(parsed_lines), 2)]
        sorted_indexes = [i + 1 for i in range(len(nested_lists)) if
                          compare_lists(nested_lists[i][0], nested_lists[i][1]) < 0]
        return sum(sorted_indexes)

    def solve_bonus_task(self, input_file_content: List[str]):
        parsed_lines = parse_input(input_file_content)
        parsed_lines.extend([[[2]], [[6]]])
        sorted_lines = sorted(parsed_lines, key=functools.cmp_to_key(compare_lists))
        return (sorted_lines.index([[2]]) + 1) * (sorted_lines.index([[6]]) + 1)

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch("(\[([\[\],\d])*\]\n?)|\n", line) for line in input_file_content)
        # does not check whether bracket-nesting is valid
