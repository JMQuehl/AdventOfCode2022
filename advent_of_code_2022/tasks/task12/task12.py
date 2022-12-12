import re
from collections import deque

from advent_of_code_2022.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List, Tuple
import numpy as np
from nptyping import NDArray
import matplotlib.pyplot as plt


class Task12(AdventOfCodeProblem):
    elevation_map: NDArray
    start: List[Tuple[int, int]]
    target: Tuple[int, int]
    distance_map: NDArray

    def __init__(self, args):
        super().__init__(args)
        self.answer_text = "The distance to the target coordinates is: %d"
        self.bonus_answer_text = "The shortest distance from an \'a\' to the goal is: %d"
        self.task_number = 12

    def parse_board(self, input_file_content: List[str]):
        shape = (len(input_file_content), len(input_file_content[0].replace('\n', '')))
        self.elevation_map = np.zeros(shape)
        self.distance_map = np.ones(shape) * shape[0] * shape[
            1]  # == the maximal number of steps without walking through the same coordinate
        self.start = []
        self.target = (0, 0)
        for i, line in enumerate(input_file_content):
            for j, letter in enumerate(line.replace('\n', '')):
                if letter == 'S':
                    self.elevation_map[i][j] = 0
                    self.start.append((i, j))
                    self.distance_map[i, j] = 0
                elif letter == 'E':
                    self.elevation_map[i][j] = ord('z') - ord('a')
                    self.target = (i, j)
                else:
                    self.elevation_map[i][j] = ord(letter) - ord('a')

    def _visit_valid_neighbors(self, coordinate: Tuple[int, int]) -> List[Tuple[int, ...]]:
        neighbors = []
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        coordinates = [tuple(map(lambda i, j: int(i + j), x, coordinate)) for x in directions]
        for neighbor_coords in coordinates:
            if 0 <= neighbor_coords[0] < len(self.elevation_map) and 0 <= neighbor_coords[1] < len(
                    self.elevation_map[0]) and self.elevation_map[neighbor_coords] <= self.elevation_map[
                coordinate] + 1 and self.distance_map[neighbor_coords] > self.distance_map[coordinate] + 1:
                neighbors.append(neighbor_coords)
                self.distance_map[neighbor_coords] = self.distance_map[coordinate] + 1
        return neighbors

    def propagate_distances_through_map(self):
        current_candidates = deque()
        for coords in self.start:
            current_candidates.extend(self._visit_valid_neighbors(coords))
        while current_candidates:
            current_candidates.extend(self._visit_valid_neighbors(current_candidates.popleft()))

    def solve_task(self, input_file_content: List[str]):
        self.parse_board(input_file_content)
        self.propagate_distances_through_map()
        if self.args.visualize:
            plt.imshow(self.elevation_map)
            plt.show()
            plt.imshow(self.distance_map)
            plt.show()
        return self.distance_map[self.target]

    def solve_bonus_task(self, input_file_content: List[str]):
        self.parse_board(input_file_content)
        self.start = []
        for x in [(i, j) for i in range(len(self.elevation_map)) for j in range(len(self.elevation_map[0])) if
                  self.elevation_map[i][j] == 0]:
            self.distance_map[x] = 0
            self.start.append(x)
        self.propagate_distances_through_map()
        return self.distance_map[self.target]

    def is_input_valid(self, input_file_content: List[str]):
        return len(input_file_content) > 0 and all(
            len(x.replace('\n', '')) == len(input_file_content[0].replace('\n', '')) for x in
            input_file_content) and all(re.fullmatch('[a-zES]+\n?', line) for line in input_file_content)
        # does not check whether only exactly one S and E exist
