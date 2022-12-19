from advent_of_code_2022.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List, Tuple
import re
import numpy as np
from nptyping import NDArray
from advent_of_code_2022.tasks.task19.solve import solve


class Blueprint:
    id: int
    costs: NDArray
    max_ore_cost: int
    current_max_found = 0

    def __init__(self, values: List[int]):
        self.id = values[0]
        self.costs = np.array([[values[1], 0, 0, 0],  # ore-robot
                               [values[2], 0, 0, 0],  # clay-robot
                               [values[3], values[4], 0, 0],  # obsidian-robot
                               [values[5], 0, values[6], 0]])  # geode-robot
        self.max_ore_cost = max(self.costs[:, 0])  # used to determine when to stop building ore-robots


class Task19(AdventOfCodeProblem):
    blueprints: List[Blueprint]

    def __init__(self, args):
        super().__init__(args)
        self.answer_text = 'The sum of quality levels of all blueprints is: %d.'
        self.bonus_answer_text = 'The product of the first three blueprints with a time horizon of 32 minutes is: %d.'
        self.task_number = 19

    def parse_input(self, input_file_content: List[str]):
        self.blueprints = []
        for line in input_file_content:
            self.blueprints.append(Blueprint([int(x) for x in re.findall('\d+', line)]))

    def evaluation_step(self, bprint: Blueprint, time_left: int, resources: NDArray, robots: NDArray,
                        intended_robot: int):
        if intended_robot == 0 and robots[0] >= bprint.max_ore_cost or \
                intended_robot == 1 and robots[1] >= bprint.costs[2, :][1] or \
                intended_robot == 2 and (robots[2] >= bprint.costs[3, :][2] or robots[1] == 0) or \
                intended_robot == 3 and robots[2] == 0 or \
                resources[-1] + robots[-1] * time_left + ((time_left - 1) * time_left // 2) <= bprint.current_max_found:
            # ensures that we stop when we have enough robots or can't reach current high-score anymore.
            return
        current_resources = resources.copy()
        while time_left > 0:
            for i in range(4):
                if intended_robot == i and (current_resources >= bprint.costs[i, :]).all():
                    new_resources = current_resources + robots - bprint.costs[i, :]
                    new_robots = robots.copy()
                    new_robots[i] += 1
                    for next_goal in range(4):
                        self.evaluation_step(bprint, time_left - 1, new_resources, new_robots, next_goal)
                    return
            time_left -= 1
            current_resources += robots
        bprint.current_max_found = max(bprint.current_max_found, current_resources[-1])
        return

    def evaluate_blueprint(self, print_id: int, time_steps: int, multiply_with_index: bool = False):
        bprint = self.blueprints[print_id - 1]
        resources = np.array([0, 0, 0, 0])  # ore, clay, obsidian, geode
        robots = np.array([1, 0, 0, 0])  # ore, clay, obsidian, geode
        max_score = 0
        for i in range(4):
            self.evaluation_step(bprint, time_steps, resources, robots, i)
            max_score = max(max_score,
                            print_id * bprint.current_max_found if multiply_with_index else bprint.current_max_found)
            bprint.current_max_found = 0
        return max_score
        # return print_id * self.evaluation_step(bprint, time_steps, resources, robots)

    def solve_task(self, input_file_content: List[str]):
        # return solve(input_file_content)
        self.parse_input(input_file_content)
        score = 0
        for i in range(len(self.blueprints)):
            bp_score = self.evaluate_blueprint(i + 1, 24, True)
            score += bp_score
        return score

    def solve_bonus_task(self, input_file_content: List[str]):
        self.parse_input(input_file_content)
        score = 1
        for i in range(min(3, len(input_file_content))):
            bp_score = self.evaluate_blueprint(i + 1, 32)
            score *= bp_score
        return score

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch(
            "Blueprint \d+: Each ore robot costs \d ore. Each clay robot costs \d ore. "
            "Each obsidian robot costs \d ore and \d+ clay. "
            "Each geode robot costs \d ore and \d+ obsidian.\n?",
            line) for line in input_file_content)
