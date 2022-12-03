from sortedcontainers import SortedList

from advent_of_code_2022.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List


def evaluate_game(opponents_input: int, your_input: int):
    return ((((your_input - opponents_input) % 3) + 1) % 3) * 3
    # this works since the winning choice has the numerical value of 1 higher than the opponent's modulo 3 shifted by 1
    # so 1 < 2 < 3 < 1
    # so ((your_input - opponents_input) % 3) evaluates to 1 if won, 0 if drawn, 2 if loss
    # + 1) % 3) rotates this to 0 = loss, 1 = draw, 2 = win
    # thereby the result is 0 for loss, 3 for draw and 6 for a win


class Task02(AdventOfCodeProblem):
    def __init__(self):
        super().__init__()
        self.answer_text = 'The sum of all your scores following the assumed strategy is: %d'
        self.bonus_answer_text = 'The sum of all your scores following the intended strategy is: %d'
        self.task_number = 2

    def solve_task(self, input_file_content: List[str]):
        your_score = 0
        for line in input_file_content:
            (opponent_play, your_play) = line.split()
            num_opponent = ord(opponent_play) - ord('A') + 1  # we assign both choices the values 1-3 for r,p,s
            num_you = ord(your_play) - ord('X') + 1
            your_score += num_you + evaluate_game(num_opponent, num_you)

        return your_score

    def solve_bonus_task(self, input_file_content: List[str]):
        your_score = 0
        for line in input_file_content:
            (opponent_play, intended_goal) = line.split()
            num_opponent = ord(opponent_play) - ord('A') + 1
            num_intended_goal = ord(intended_goal) - ord('Y')  # -1 if loss, 0 if draw, 1 if win
            num_you = ((
                                   num_opponent - 1 + num_intended_goal) % 3) + 1  # assigns the numerical value of the intended choice
            your_score += num_you + (num_intended_goal + 1) * 3  # result is already known, so no evaluation necessary

        return your_score

    def is_input_valid(self, input_file_content: List[str]):
        for line in input_file_content:
            split_line = line.split()
            if not len(split_line) == 2 or split_line[0] not in ['A', 'B', 'C'] or split_line[1] not in ['X', 'Y', 'Z'] :
                return False
        return True
