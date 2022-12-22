from advent_of_code_2022.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List
import re
import numpy as np
from nptyping import NDArray
from itertools import cycle


class Task22(AdventOfCodeProblem):
    board: NDArray
    turn_list = List[int]
    number_list = List[str]
    turn_right = np.array([[0, -1], [1, 0]])
    turn_left = np.array([[0, 1], [-1, 0]])

    def __init__(self, args):
        super().__init__(args)
        self.answer_text = 'The final password is: %d.'
        self.bonus_answer_text = '%d.'
        self.task_number = 22

    def parse_input(self, input_file_content: List[str]):
        board_strings = []
        max_length = 0
        for line in input_file_content:
            if re.fullmatch(' *[.#]+ *\n?', line):
                pure_line = line.replace('\n', '')
                max_length = max(max_length, len(pure_line))
                board_strings.append(pure_line)
            elif re.fullmatch('\n?', line):
                self.board = np.zeros((len(board_strings), max_length))
                for i, line in enumerate(board_strings):
                    for j, str in enumerate(line):
                        if str == '.':
                            self.board[i][j] = 1  # free = 1
                        elif str == '#':
                            self.board[i][j] = 2  # wall = 2
            else:
                self.number_list = [int(x) for x in re.findall('\d+', line)]
                self.turn_list = re.findall('[RL]', line)

    def go(self, start: NDArray, direction: NDArray, distance: int) -> NDArray:
        current_location = start
        next_location = current_location + direction
        for i in range(distance):
            while self.board[next_location[0]][next_location[1]] == 0:
                next_location = (next_location + direction) % np.array(
                    [len(self.board), len(self.board[next_location[0]])])
            if self.board[next_location[0]][next_location[1]] == 2:  # found wall
                return current_location
            if self.board[next_location[0]][next_location[1]] == 1:  # go there
                current_location = next_location
                next_location = (next_location + direction) % np.array(
                    [len(self.board), len(self.board[next_location[0]])])
        return current_location

    def rotate(self, direction: NDArray, rotation: str) -> NDArray:
        return np.dot(direction, self.turn_right) if rotation == 'R' else np.dot(direction, self.turn_left)

    def follow_instructions(self):
        current_direction = np.array([0, 1])
        current_location = self.go(np.array([0, 0]), current_direction, 1)
        for i, instruction in enumerate(self.number_list):
            current_location = self.go(current_location, current_direction, instruction)
            if i < len(self.turn_list):
                current_direction = self.rotate(current_direction, self.turn_list[i])
        return current_location, current_direction

    def solve_task(self, input_file_content: List[str]):
        self.parse_input(input_file_content)
        last_location, last_direction = self.follow_instructions()
        if all(last_direction == np.array([0, 1])):  # right
            direction_value = 0
        elif all(last_direction == np.array([1, 0])):  # down
            direction_value = 1
        elif all(last_direction == np.array([0, -1])):  # left
            direction_value = 2
        else:  # up
            direction_value = 3
        return (last_location[0] + 1) * 1000 + (last_location[1] + 1) * 4 + direction_value

    def solve_bonus_task(self, input_file_content: List[str]):
        self.parse_input(input_file_content)
        return 0

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch('( *[.#]+ *\n?)|(\n?)|([\dRL]+\n?)', line) for line in input_file_content)
