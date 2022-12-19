from advent_of_code_2022.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List, Set, Tuple
import re
from nptyping import NDArray


def get_neighbors(coordinate: Tuple[int, int, int]):
    relative_coordinates = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
    return [(coordinate[0] + x[0], coordinate[1] + x[1], coordinate[2] + x[2]) for x in
            relative_coordinates]


class Task18(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = 'The surface area of the scanned lava droplet is %d.'
        self.bonus_answer_text = 'The surface area of the scanned lava droplet without air pockets is %d.'
        self.task_number = 18

    droplet: NDArray
    coordinates: Set
    air_coordinates: Set
    max_values: Tuple[int, int, int]

    def parse_input(self, input_file_content: List[str]):
        max_x = max_y = max_z = 0
        self.coordinates = set()
        for line in input_file_content:
            coordinate = [int(x) for x in re.findall('\d+', line)]
            self.coordinates.add((coordinate[0], coordinate[1], coordinate[2]))
            max_x = max(max_x, coordinate[0])
            max_y = max(max_y, coordinate[1])
            max_z = max(max_z, coordinate[2])
        self.max_values = (max_x + 1, max_y + 1, max_z + 1)

    def get_number_of_neighbors(self, coordinate: Tuple[int, int, int]):
        return len([x for x in get_neighbors(coordinate) if x in self.coordinates])

    def get_number_of_air_neighbors(self, coordinate: Tuple[int, int, int]):
        return len([x for x in get_neighbors(coordinate) if x in self.air_coordinates])

    def fill_with_air(self, start_coordinate: Tuple[int, int, int]):
        self.air_coordinates = set()
        self.air_coordinates.add(start_coordinate)
        candidates = set(get_neighbors(start_coordinate))
        while candidates:
            candidate = candidates.pop()
            if candidate not in self.coordinates and \
                    -2 < candidate[0] <= self.max_values[0] and \
                    -2 < candidate[1] <= self.max_values[1] and \
                    -2 < candidate[2] <= self.max_values[2]:
                self.air_coordinates.add(candidate)
                for x in get_neighbors(candidate):
                    if x not in self.coordinates and x not in self.air_coordinates:
                        candidates.add(x)

    def solve_task(self, input_file_content: List[str]):
        self.parse_input(input_file_content)
        number_of_visible_sides = 0
        for coordinate in self.coordinates:
            number_of_visible_sides += 6 - self.get_number_of_neighbors(coordinate)
        return number_of_visible_sides

    def solve_bonus_task(self, input_file_content: List[str]):
        self.parse_input(input_file_content)
        self.fill_with_air((0, 0, 0))
        number_of_outside_sides = 0
        for coordinate in self.coordinates:
            number_of_outside_sides += self.get_number_of_air_neighbors(coordinate)
        return number_of_outside_sides

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch("[0-9]+,[0-9]+,[0-9]+\n?", line) for line in input_file_content)
