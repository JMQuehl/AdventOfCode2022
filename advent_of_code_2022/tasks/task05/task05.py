from advent_of_code_2022.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List
import re
from collections import deque
import copy

board_line_re = "((\[[A-Z]\] )|( {4}))*((\[[A-Z]\])|( {3}))\n*"
index_line_re = "( [1-9] {2})*( [1-9] )\n*"
instructions_re = "move [1-9][0-9]* from [1-9] to [1-9]\n*"


def is_board_valid(board_input: List[str]):
    if len(board_input) < 1:
        return False  # Even an empty board needs indexes
    if not re.fullmatch(index_line_re, board_input[-1]):
        return False  # the index line is not built correctly
    board_indexes = [int(x) for x in board_input[-1].split()]
    if board_indexes != list(range(1, len(board_indexes) + 1)):
        return False  # indexes are not ascending
    for line in board_input[0:len(board_input) - 2]:
        if not len(line.replace('\n', '')) == (4 * board_indexes[-1]) - 1 or not re.fullmatch(
                board_line_re, line):
            return False  # line does not match pattern.
    # note: We don't check if below each box is another box.
    return True


def are_move_instructions_valid(move_input: List[str]):
    for line in move_input:
        if not re.fullmatch(instructions_re, line):
            return False
    return True


def visualize_board(board: List[deque[str]]):
    index_str = ""
    for i in range(1, len(board) + 1):
        index_str += " %d  " % i
    string_list = [index_str[:-1]]  # because we added a ' ' too much
    list_copy = copy.deepcopy(board)
    while not all([len(x) == 0 for x in list_copy]):  # while not all entries in the board are empty
        current_line = ""
        for queue in list_copy:
            if len(queue) == 0:
                current_line += "    "
            else:
                current_line += "[%s] " % queue.popleft()
        string_list.append(current_line[:-1])
    for line in string_list[::-1]:
        print(line)


class Task05(AdventOfCodeProblem):
    initial_board: List[deque[str]]
    current_board: List[deque[str]]
    movement_instructions: List[List[int]]  # each inner list contains 3 numbers (how many, from, to)

    def __init__(self):
        super().__init__()
        self.answer_text = 'The top crates have the identifiers: %s'
        self.bonus_answer_text = 'Using the CrateMover9001, the top crates have the identifiers: %s'
        self.task_number = 5

    def parse_board(self, board_input: List[str]):
        board_size = len(board_input[0]) // 4
        self.initial_board = []
        for i in range(board_size):
            self.initial_board.append(deque())
        # note: we assume that the validity check is done beforehand, so the board size can be checked by each line.
        for line in board_input:
            if re.fullmatch(board_line_re, line):
                for i in range(board_size):
                    identifier = line[1 + i * 4]
                    if not identifier == ' ':
                        self.initial_board[i].appendleft(identifier)
            else:
                break
        pass

    def parse_instructions(self, instruction_input: List[str]):
        self.movement_instructions = []
        for line in instruction_input:
            if re.fullmatch(instructions_re, line):
                split_line = line.split()
                self.movement_instructions.append([int(split_line[1]), int(split_line[3]), int(split_line[5])])

    def solve_task(self, input_file_content: List[str]):
        self.parse_board(input_file_content)
        self.parse_instructions(input_file_content)
        self.current_board = copy.deepcopy(self.initial_board)
        for instruction in self.movement_instructions:
            for i in range(instruction[0]):
                self.current_board[instruction[2] - 1].append(self.current_board[instruction[1] - 1].pop())
        return_string = ""
        for stack in self.current_board:
            return_string += stack[-1]
        return return_string

    def solve_bonus_task(self, input_file_content: List[str]):
        self.parse_board(input_file_content)
        self.parse_instructions(input_file_content)
        self.current_board = copy.deepcopy(self.initial_board)
        for instruction in self.movement_instructions:
            stack = []
            for i in range(instruction[0]):
                stack.append(self.current_board[instruction[1] - 1].pop())
            for item in stack[::-1]:
                self.current_board[instruction[2] - 1].append(item)
        return_string = ""
        for stack in self.current_board:
            return_string += stack[-1]
        return return_string

    def is_input_valid(self, input_file_content: List[str]):
        pure_input = [x.replace('\n', '') for x in input_file_content]  # we ignore that \n could be at any index
        if len(pure_input) == 0:
            return False
        board_separator_line_index = len(pure_input) - 1
        for i in range(len(pure_input)):
            if pure_input[i] == "":
                board_separator_line_index = i
                break
        board = pure_input[0:board_separator_line_index]
        move_instructions = [] if (board_separator_line_index == len(pure_input) - 1) else pure_input[
                                                                                           board_separator_line_index + 1:]
        return is_board_valid(board) and are_move_instructions_valid(move_instructions)
