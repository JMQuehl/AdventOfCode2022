import re

import matplotlib.pyplot as plt

from advent_of_code_2022.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List
import numpy as np
from nptyping import NDArray


class Task14(AdventOfCodeProblem):
    cave: NDArray
    x_offset: int

    def __init__(self, args):
        super().__init__(args)
        self.answer_text = "%d units of sand are caught before sand falls into the abyss."
        self.bonus_answer_text = "The source is blocked after %d units of sand."
        self.task_number = 14

    def assign_to_coordinate(self, coordinate: NDArray, value: int):
        self.cave[coordinate[0] + self.x_offset][coordinate[1]] = value

    def get_from_cave(self, coordinate: NDArray) -> int:
        return self.cave[coordinate[0] + self.x_offset][coordinate[1]] if 0 <= coordinate[0] + self.x_offset < len(
            self.cave) and 0 <= coordinate[1] < len(self.cave[0]) else 0

    def parse_input(self, input_file_content: List[str]):
        coordinates = []
        for line in input_file_content:
            coordinates.append([np.asarray([int(y) for y in x.split(',')]) for x in line.split(" -> ")])
        min_x = max_x = 500
        min_y = max_y = 0
        for rock_structure in coordinates:
            for rock_edge in rock_structure:
                min_x = min(min_x, rock_edge[0])
                max_x = max(max_x, rock_edge[0])
                min_y = min(min_y, rock_edge[1])
                max_y = max(max_y, rock_edge[1])
        y_length = max_y - min_y + 3
        min_x = min(min_x, 500 - (y_length + 1))
        max_x = max(max_x, 500 + (y_length + 1))
        x_length = max(max_x - min_x + 3, 500 - min_x)
        cave_shape = (x_length, y_length)
        self.cave = np.zeros(cave_shape)
        self.x_offset = -min_x + 1
        for rock_structure in coordinates:
            current_edge = rock_structure[0]
            for rock_edge in rock_structure:
                direction = np.sign(rock_edge - current_edge)
                while any(current_edge != rock_edge):
                    self.assign_to_coordinate(current_edge, 2)
                    current_edge += direction
            self.assign_to_coordinate(current_edge, 2)
        self.cave[:, -1] = 2

    def pur_sand(self, start_coordinate: NDArray) -> bool:
        current_coordinate = start_coordinate
        valid_fall_directions = [np.asarray([0, 1]), np.asarray([-1, 1]), np.asarray([1, 1])]
        for i in range(start_coordinate[1], len(self.cave[0])):
            free_coordinates = [x + current_coordinate for x in valid_fall_directions if
                                self.get_from_cave(x + current_coordinate) == 0]
            if not free_coordinates:
                self.assign_to_coordinate(current_coordinate, 1)
                # self.cave[current_coordinate] = 1
                return current_coordinate[1] == len(self.cave[0]) - 2
            current_coordinate = free_coordinates[0]
        return True

    def visualize_cave(self):
        color_map = {0: np.array([255, 255, 255]),  # white = empty areas
                     1: np.array([190, 160, 80]),  # beige = sand
                     2: np.array([0, 0, 0])}  # black = structures
        img_data = np.ndarray(shape=(self.cave.T.shape[0], self.cave.T.shape[1], 3), dtype=int)
        for i in range(self.cave.T.shape[0]):
            for j in range(self.cave.T.shape[1]):
                img_data[i, j] = color_map[self.cave.T[i][j]]
        plt.imshow(img_data)
        plt.show()

    def solve_task(self, input_file_content: List[str]):
        self.parse_input(input_file_content)
        i = 0
        while not self.pur_sand(np.asarray([500, 0])):
            i += 1
        if self.args.visualize:
            self.visualize_cave()
        return i

    def solve_bonus_task(self, input_file_content: List[str]):
        self.parse_input(input_file_content)
        i = 0
        while self.get_from_cave(np.asarray([500, 0])) == 0:
            self.pur_sand(np.asarray([500, 0]))
            i += 1
        if self.args.visualize:
            self.visualize_cave()
        return i

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch("(\d+,\d+)( -> \d+,\d+)*\n?", line) for line in input_file_content)
