import re
from advent_of_code_2022.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List, Dict
from sortedcontainers import SortedList


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
        if time_left <= 0:
            return 0
        dist_map = self.distance_maps[starting_valve]
        max_flow = 0
        for target in interesting_nodes_left:
            list_copy = list(interesting_nodes_left)
            list_copy.remove(target)
            max_flow = max(max_flow, self.calc_max_flow(target, time_left - dist_map[target] - 1, list_copy))
        return max_flow + (time_left * self.valves[starting_valve].flow_rate)

    def two_agents_calc_max_flow(self, starting_valve1: str, starting_valve2: str, time_left: int,
                                 interesting_nodes_left: List[str], time_left_for1, time_left_for2, history1, history2):
        if time_left <= 0:
            return 0
        dist_map1 = self.distance_maps[starting_valve1]
        dist_map2 = self.distance_maps[starting_valve2]
        max_flow = 0
        max_flow = max(max_flow, self.calc_max_flow(starting_valve1, time_left - time_left_for1,
                                                    interesting_nodes_left))  # from here onwards only 1 acts
        max_flow = max(max_flow, self.calc_max_flow(starting_valve2, time_left - time_left_for2,
                                                    interesting_nodes_left))  # from here onwards only 2 acts

        for target1 in interesting_nodes_left:
            list_copy = list(interesting_nodes_left)
            list_copy.remove(target1)
            if time_left_for1 == time_left_for2 == 0:  # both act
                for target2 in [x for x in interesting_nodes_left if x != target1]:
                    hist_copy1 = list(history1)
                    hist_copy2 = list(history2)
                    list_copy.remove(target2)

                    hist_copy1.append(target1)
                    hist_copy2.append(target2)

                    time_till_next = min(dist_map1[target1], dist_map2[target2]) + 1
                    max_flow = max(max_flow,
                                   self.two_agents_calc_max_flow(target1, target2, time_left - time_till_next,
                                                                 list_copy,
                                                                 dist_map1[target1] + 1 - time_till_next,
                                                                 dist_map2[target2] + 1 - time_till_next, hist_copy1,
                                                                 hist_copy2))
            elif time_left_for1 == 0:  # only 1 acts

                hist_copy1 = list(history1)
                hist_copy2 = list(history2)
                time_till_next = min(time_left_for2, dist_map1[target1] + 1)
                hist_copy1.append(target1)
                max_flow = max(max_flow,
                               self.two_agents_calc_max_flow(target1, starting_valve2, time_left - time_till_next,
                                                             list_copy, dist_map1[target1] + 1 - time_till_next,
                                                             time_left_for2 - time_till_next, hist_copy1, hist_copy2))
            else:

                hist_copy1 = list(history1)
                hist_copy2 = list(history2)

                time_till_next = min(time_left_for1, dist_map2[target1] + 1)
                hist_copy2.append(target1)
                max_flow = max(max_flow,
                               self.two_agents_calc_max_flow(starting_valve1, target1, time_left - time_till_next,
                                                             list_copy, time_left_for1 - time_till_next,
                                                             dist_map2[target1] + 1 - time_till_next, hist_copy1,
                                                             hist_copy2))

        if time_left_for1 == time_left_for2 == 0:
            return max_flow + (
                    time_left * (self.valves[starting_valve1].flow_rate + self.valves[starting_valve2].flow_rate))
        elif time_left_for1 == 0:
            return max_flow + (time_left * self.valves[starting_valve1].flow_rate)
        else:
            return max_flow + (time_left * self.valves[starting_valve2].flow_rate)

        # TODO: Debuggen - evtl jeweils eine history für 1 und 2 mitgeben, und gucken, ob der richtige Fall überprüft wird.

    def solve_task(self, input_file_content: List[str]):
        self.parse_input(input_file_content)
        self.calculate_distance_maps()
        return self.calc_max_flow('AA', 30, self.interesting_valves)

    def solve_bonus_task(self, input_file_content: List[str]):
        self.parse_input(input_file_content)
        self.calculate_distance_maps()
        returnvalue = self.two_agents_calc_max_flow('AA', 'AA', 26, self.interesting_valves, 0, 0, ['AA'], ['AA'])
        return returnvalue

    def is_input_valid(self, input_file_content: List[str]):
        return all(
            re.fullmatch("Valve [A-Z]{2} has flow rate=\d+; tunnels? leads? to valves? [A-Z]{2}(, [A-Z]{2})*\n?", line)
            for line in input_file_content)
