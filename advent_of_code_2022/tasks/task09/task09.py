from advent_of_code_2022.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List
import re
import numpy as np
from nptyping import NDArray

def visualize_history(history: List[NDArray]):
    min_x = min_y = max_x = max_y = 0
    for coord in history:
        max_x = max(max_x, coord[0])
        min_x = min(min_x, coord[0])
        max_y = max(max_y, coord[1])
        min_y = min(min_y, coord[1])
    print("board of size: %d, %d" % (max_x - min_x + 1, max_y - min_y + 1))
    board = np.zeros((max_x - min_x + 1, max_y - min_y + 1))
    for i in range(len(history)):
        x, y = history[i] - np.asarray([min_x, min_y])
        board[x][y] = i
    print(board)


class Task09(AdventOfCodeProblem):
    direction_dict = dict(R=np.asarray((0, 1)), L=np.asarray((0, -1)), U=np.asarray((-1, 0)), D=np.asarray((1, 0)))

    def __init__(self, args):
        super().__init__(args)
        self.answer_text = 'The tail visited %d unique locations.'
        self.bonus_answer_text = '%d'
        self.task_number = 9

    def parse_head_history(self, input_file_content: List[str]) -> List[NDArray] :
        current_h = np.asarray((0, 0))
        position_history_h = [current_h]
        for line in input_file_content:
            direction, number = line.split()
            number = int(number)
            direction = self.direction_dict[direction]
            position_history_h.extend([current_h + x * direction for x in range(1, number + 1)])
            current_h = position_history_h[-1]
        return position_history_h


    def follow_head(self, history_h: List[NDArray]) -> List[NDArray]:
        current_pos = history_h[0]
        history_t = [current_pos]
        for pos in history_h:
            diff = pos - current_pos
            if np.amax(np.abs(diff)) > 1:
                current_pos = current_pos + np.sign(diff)
                history_t.append(current_pos)
        return history_t

    def solve_task(self, input_file_content: List[str]):
        position_history_h = self.parse_head_history(input_file_content)
        history_t = self.follow_head(position_history_h)
        if self.args.visualize:
            print("head_history:")
            visualize_history(position_history_h)
            print("tail_history:")
            visualize_history(history_t)
        return len(set([tuple(x) for x in history_t]))

    def solve_bonus_task(self, input_file_content: List[str]):
        hist = self.parse_head_history(input_file_content)
        for i in range(9):
            hist = self.follow_head(hist)
        return len(set([tuple(x) for x in hist]))

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch("[RLUD] \d+\n?", line) for line in input_file_content)
