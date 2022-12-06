import argparse
import sys
from advent_of_code_2022.TaskFactory import create_all_tasks, create_single_task


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", "-t", default="0", type=int, help="Which task to display. Default = 0 for all tasks.")
    parser.add_argument("--display", "-d", default=False, type=bool,
                        help="Should the task be displayed in a web browser?")

    args = parser.parse_args()

    if args.task == 0:
        tasks = create_all_tasks()
        print("Loading all tasks...")
    else:
        tasks = [create_single_task(args.task)]
        print("Loading task number %02d" % args.task)

    for task in tasks:
        print()
        task.print_answer_to_task()
        if args.display:
            task.render_description()
    return 0


if __name__ == '__main__':
    sys.exit(main())
