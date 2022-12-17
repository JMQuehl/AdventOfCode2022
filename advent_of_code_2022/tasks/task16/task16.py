import re
from advent_of_code_2022.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List, Dict
from sortedcontainers import SortedList
from itertools import combinations, chain


class Valve:
    identifier: str
    flow_rate: int
    neighbors: List[str]

    def __init__(self, identifier: str, flow_rate=0, neighbors=None):
        if neighbors is None:
            neighbors = []
        self.identifier = identifier
        self.flow_rate = flow_rate
        self.neighbors = neighbors


class Task16(AdventOfCodeProblem):
    valves: Dict[str, Valve]
    distance_maps: Dict[str, Dict]
    interesting_valves: List[str]

    def __init__(self, args):
        super().__init__(args)
        self.answer_text = "You can release at most %d pressure."
        self.bonus_answer_text = "Working together with the elephant, you can release at most %d pressure."
        self.task_number = 16

    def parse_input(self, input_file_content: List[str]):
        self.valves = {}
        self.interesting_valves = []
        for line in input_file_content:
            name_list = re.findall(r'[A-Z]{2}', line)
            flow_rate = int(re.findall(r'\d+', line)[0])
            valve = Valve(name_list[0], flow_rate, name_list[1:])
            self.valves[valve.identifier] = valve
            if valve.flow_rate > 0:
                self.interesting_valves.append(valve.identifier)

    def calculate_distance_map(self, valve_id: str):
        dist_map = {valve_id: 0}
        visited = [valve_id]
        can_visit = SortedList([(1, x) for x in self.valves[valve_id].neighbors], key=lambda x: x[0])
        while len(can_visit) > 0:
            dist, current_valve = can_visit.pop(0)
            dist_map[current_valve] = dist
            for neighbor in [x for x in self.valves[current_valve].neighbors if x not in visited]:
                can_visit.add((dist + 1, neighbor))
            visited.append(current_valve)
        self.distance_maps[valve_id] = dist_map

    def calculate_distance_maps(self):
        self.distance_maps = {}
        self.calculate_distance_map('AA')
        for valve_id in self.interesting_valves:
            self.calculate_distance_map(valve_id)

    def calc_max_flow(self, starting_valve: str, time_left: int, interesting_nodes_left: List[str]):
        if time_left < 0:
            return 0
        dist_map = self.distance_maps[starting_valve]
        max_flow = 0
        for target in interesting_nodes_left:
            list_copy = list(interesting_nodes_left)
            list_copy.remove(target)
            max_flow = max(max_flow, self.calc_max_flow(target, time_left - dist_map[target] - 1, list_copy))
        return max_flow + (time_left * self.valves[starting_valve].flow_rate)

    def calc_max_flow_with_two_actors(self, time_left: int):
        all_splits = [x for a in range(len(self.interesting_valves)) for x in combinations(self.interesting_valves, a)]
        max_flow = 0
        print('checking %d combinations' % (len(all_splits) // 2 + 1))
        for i in range(len(all_splits) // 2 + 1):
            interesting1 = list(chain(all_splits[i]))
            interesting2 = [x for x in self.interesting_valves if x not in all_splits[i]]
            flow1 = self.calc_max_flow('AA', time_left, interesting1)
            flow2 = self.calc_max_flow('AA', time_left, interesting2)
            max_flow = max(max_flow, flow1 + flow2)
            print('%s and %s generate together %d flow. Current max is: %d' % (str(interesting1), str(interesting2), flow1+flow2, max_flow))
        return max_flow

    def solve_task(self, input_file_content: List[str]):
        self.parse_input(input_file_content)
        self.calculate_distance_maps()
        return self.calc_max_flow('AA', 30, self.interesting_valves)

    def solve_bonus_task(self, input_file_content: List[str]):
        self.parse_input(input_file_content)
        self.calculate_distance_maps()
        return self.calc_max_flow_with_two_actors(26)

    def is_input_valid(self, input_file_content: List[str]):
        return all(
            re.fullmatch("Valve [A-Z]{2} has flow rate=\d+; tunnels? leads? to valves? [A-Z]{2}(, [A-Z]{2})*\n?", line)
            for line in input_file_content)
