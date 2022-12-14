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
        self.bonus_answer_text = "%d"
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
        cave_shape = (max_x - min_x + 3, max_y - min_y + 3)
        self.cave = np.zeros(cave_shape)
        self.x_offset = -min_x + 1
        for rock_structure in coordinates:
            current_edge = rock_structure[0]
            for rock_edge in rock_structure:
                direction = np.sign(rock_edge - current_edge)
                while any(current_edge != rock_edge):
                    self.assign_to_coordinate(current_edge, 5)
                    current_edge += direction
            self.assign_to_coordinate(current_edge, 5)

    def pur_sand(self, start_coordinate: NDArray) -> bool:
        current_coordinate = start_coordinate
        fall_path = [start_coordinate]
        valid_fall_directions = [np.asarray([0, 1]), np.asarray([-1, 1]), np.asarray([1, 1])]
        for i in range(start_coordinate[1], len(self.cave[0])):
            free_coordinates = [x + current_coordinate for x in valid_fall_directions if
                                self.get_from_cave(x + current_coordinate) == 0]
            if not free_coordinates:
                self.assign_to_coordinate(current_coordinate, 1)
                # self.cave[current_coordinate] = 1
                return False
            current_coordinate = free_coordinates[0]
            fall_path.append(current_coordinate)
        return True

    def solve_task(self, input_file_content: List[str]):
        self.parse_input(input_file_content)
        i = 0
        while not self.pur_sand(np.asarray([500, 0])):
            i += 1
        if self.args.visualize:
            plt.imshow(self.cave.T)
            plt.show()
        return i

    def solve_bonus_task(self, input_file_content: List[str]):
        self.parse_input(input_file_content)
        plt.imshow(self.cave.T)
        plt.show()
        return 0

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch("(\d+,\d+)( -> \d+,\d+)*\n?", line) for line in input_file_content)
