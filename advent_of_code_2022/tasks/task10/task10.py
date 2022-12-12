from advent_of_code_2022.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List
import re


def get_next_values(input_string: str, current_val: int):
    if re.fullmatch("noop\n?", input_string):
        return [current_val]
    return [current_val, current_val + int(input_string.split()[1])]


class Task10(AdventOfCodeProblem):
    full_signal: List[int]

    def __init__(self, args):
        super().__init__(args)
        self.answer_text = 'The sum of the relevant signal strengths is: %d'
        self.bonus_answer_text = 'The rendered CRT-output is:\n%s'
        self.task_number = 10

    def parse_input(self, input_file_content: List[str]):
        self.full_signal = [1, 1]
        for line in input_file_content:
            self.full_signal.extend(get_next_values(line, self.full_signal[-1]))

    def render_crt(self) -> str:
        index_offset = 1
        output = ''
        for i in range(6):
            for pixel_pos in range(40):
                output += '#' if abs(self.full_signal[pixel_pos + index_offset] - pixel_pos) < 2 else '.'
            output += '\n'
            index_offset += 40
        return output

    def solve_task(self, input_file_content: List[str]):
        self.parse_input(input_file_content)
        return self.full_signal[20] * 20 + self.full_signal[60] * 60 + self.full_signal[100] * 100 + \
               self.full_signal[140] * 140 + self.full_signal[180] * 180 + self.full_signal[220] * 220

    def solve_bonus_task(self, input_file_content: List[str]):
        self.parse_input(input_file_content)
        return self.render_crt()

    def is_input_valid(self, input_file_content: List[str]):
        return all([re.fullmatch("((noop)|(addx -?\d+))\n?", line) for line in input_file_content])
        # not checked if input contains instructions for enough cpu cycles.
