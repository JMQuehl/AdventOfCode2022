import sys
import advent_of_code_utils as utils
from AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List


def create_single_task(task_number: int, args) -> AdventOfCodeProblem:
    if utils.task_exists(task_number):
        module_name = 'tasks.task%02d.task%02d' % (task_number, task_number)
        __import__(module_name)
        task = sys.modules[module_name]
        task_class = getattr(task, 'Task%02d' % task_number)
        return task_class(args)


def create_all_tasks(args) -> List[AdventOfCodeProblem]:
    i = 1
    all_tasks = []
    while utils.task_exists(i):
        all_tasks.append(create_single_task(i, args))
        i += 1
    return all_tasks
