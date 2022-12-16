import re
from advent_of_code_2022.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List, Tuple


class Task15(AdventOfCodeProblem):
    sensor_results: List[Tuple[Tuple[int, int], int]]
    beacon_positions: List[Tuple[int, int]]
    max_x: int
    max_y: int
    min_x: int
    min_y: int

    def __init__(self, args):
        super().__init__(args)
        self.answer_text = "In the row with y=2000000 %d positions cannot contain a beacon."
        self.bonus_answer_text = "The tuning frequency is: %d"
        self.task_number = 15

    def parse_input(self, input_file_content: List[str]):
        self.sensor_results = []
        self.beacon_positions = []
        self.min_x = self.min_y = self.max_x = self.max_y = 0
        for line in input_file_content:
            scanline = list(map(int, re.findall(r'-?\d+', line)))
            scanned_area = abs(scanline[2] - scanline[0]) + abs(scanline[3] - scanline[1])
            self.min_x = min(self.min_x, scanline[0] - scanned_area)
            self.min_y = min(self.min_y, scanline[1] - scanned_area)
            self.max_x = max(self.max_x, scanline[0] + scanned_area)
            self.max_y = max(self.max_y, scanline[1] + scanned_area)
            self.sensor_results.append(((scanline[0], scanline[1]), scanned_area))
            self.beacon_positions.append((scanline[2], scanline[3]))

    def get_impossible_areas(self, row_number: int, limit_x_range: bool, x_range=(0, 4000000)) -> List[List[int]]:
        impossible_areas = []
        for scanline in self.sensor_results:
            length_in_line = scanline[1] - abs(scanline[0][1] - row_number)
            if length_in_line >= 0:  # if sensor in scanline has reach into row
                if limit_x_range:
                    impossible_area = [max(x_range[0], scanline[0][0] - length_in_line),
                                       min(x_range[1], scanline[0][0] + length_in_line)]
                else:
                    impossible_area = [scanline[0][0] - length_in_line, scanline[0][0] + length_in_line]
                merged = False
                for area in list(impossible_areas):  # find if sensor_area should be merged into existing area
                    if impossible_area[0] <= area[0] <= impossible_area[1] or \
                            area[0] <= impossible_area[0] <= area[1]:  # there is overlap
                        if not merged:
                            area[0] = min(area[0], impossible_area[0])
                            area[1] = max(area[1], impossible_area[1])
                            merged = True
                            impossible_area = area
                        else:
                            impossible_area[0] = min(area[0], impossible_area[0])
                            impossible_area[1] = max(area[1], impossible_area[1])
                            impossible_areas.remove(area)
                if not merged:
                    impossible_areas.append(impossible_area)
        return impossible_areas

    def get_impossible_positions(self, row_number: int) -> list[list[int]]:
        impossible_areas = self.get_impossible_areas(row_number, False)
        beacons_in_line = [x for x in self.beacon_positions if x[1] == row_number]
        beacons_in_areas = []
        return_areas = []

        for impossible_area in impossible_areas:
            beacons_in_area = []
            for beacon in list(beacons_in_line):
                if impossible_area[0] <= beacon[0] <= impossible_area[1]:  # beacon in area -> split area
                    beacons_in_area.append(beacon)
                    # beacons_in_line.remove(beacon) # probably makes this less efficient since remove() is costly
            if beacons_in_area:
                beacons_in_areas.append((impossible_area, sorted(beacons_in_area, key=lambda x: x[0])))
            else:
                return_areas.append(impossible_area)

        for area, beacons in beacons_in_areas:
            current_area = area
            for beacon in beacons:
                if current_area[0] == beacon[0]:
                    current_area[0] = current_area[0] + 1
                elif current_area[0] < beacon[0]:
                    return_areas.append([current_area[0], beacon[0] - 1])
                    current_area[0] = beacon[0] + 1
            if not current_area[1] < current_area[0]:
                return_areas.append(current_area)
        return return_areas

    def find_possible_position_in_range(self, upper_limit: int) -> Tuple[int, int]:
        for i in range(upper_limit + 1):
            impossible_areas = self.get_impossible_areas(i, True, (0, upper_limit))
            if len(impossible_areas) > 1:
                return sorted(impossible_areas, key=lambda x: x[0])[0][1] + 1, i
        return -1, -1

    def solve_task(self, input_file_content: List[str]):
        self.parse_input(input_file_content)
        impossible_areas = self.get_impossible_positions(2000000)
        return sum([x[1] - x[0] + 1 for x in impossible_areas])

    def solve_bonus_task(self, input_file_content: List[str]):
        self.parse_input(input_file_content)
        position = self.find_possible_position_in_range(4000000)
        return (position[0] * 4000000) + position[1]

    def is_input_valid(self, input_file_content: List[str]):
        return all(
            re.fullmatch("Sensor at x=-?\d+, y=-?\d+: closest beacon is at x=-?\d+, y=-?\d+\n?", line) for line in
            input_file_content)
