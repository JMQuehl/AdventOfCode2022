import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from advent_of_code_2022.TaskFactory import create_all_tasks, create_single_task
from advent_of_code_2022.advent_of_code_utils import parse_args

def main() -> int:
    args = parse_args(sys.argv[1:])
    if args.task == 0:
        tasks = create_all_tasks(args)
        print("Loading all tasks...")
    else:
        tasks = [create_single_task(args.task, args)]
        print("Loading task number %02d" % args.task)

    for task in tasks:
        print()
        task.print_answer_to_task()
        if args.display:
            task.render_description()
    return 0


if __name__ == '__main__':
    sys.exit(main())
