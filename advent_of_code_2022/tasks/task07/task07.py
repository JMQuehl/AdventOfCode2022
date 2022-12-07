from advent_of_code_2022.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List
import re

valid_res = ["\$ ls",  # valid ls command
             "\$ cd (/|(\w)+|..)",  # valid cd command
             "dir \w+",  # valid ls output of dir
             "[1-9][0-9]* \w+(.\w+)?"]  # valid ls output of file


class SimpleFileTreeNode:
    # Note: In order to keep this short, we will not create different classes for files and folders
    children: List['SimpleFileTreeNode']
    parent: 'SimpleFileTreeNode'
    size: int
    is_folder: bool
    name: str

    full_path: str  # unique identifier for each node

    def __init__(self, name: str, is_folder=True, size=0, parent=None):
        self.name = name
        self.children = []
        self.is_folder = is_folder
        self.size = size
        self.parent = parent
        self.full_path = "%s/%s" % (self.parent.full_path, self.name) if self.parent else self.name
        if self.parent:
            self.parent._update_folder_size(size)
        # this implementation allows folders to have a size, which is ok in this context and can be used for buffering.

    def add_child_node(self, name: str, is_folder=True, size=0) -> 'SimpleFileTreeNode':
        new_node = SimpleFileTreeNode(name=name, is_folder=is_folder, size=size, parent=self)
        self.children.append(new_node)
        return new_node

    def print_files(self, suffix=""):
        print_string = suffix + "- %s " % self.name
        if self.is_folder:
            print_string += "(dir)"
        else:
            print_string += "(file, size=%d)" % self.size
        print(print_string)
        for child_node in self.children:
            child_node.print_files(suffix + "  ")

    def traverse(self, target_node_name: str) -> 'SimpleFileTreeNode':
        if target_node_name == "..":
            return self.parent if self.parent else self
        else:
            if target_node_name in [x.name for x in self.children]:
                return [x for x in self.children if x.name == target_node_name][0]  # names are unique
            else:
                return self.add_child_node(name=target_node_name)

    def _update_folder_size(self, size_diff: int):
        self.size += size_diff
        if self.parent:
            self.parent._update_folder_size(size_diff)

    def __eq__(self, other):
        return self.full_path == other.full_path if isinstance(other, SimpleFileTreeNode) else False


class Task07(AdventOfCodeProblem):
    file_tree: SimpleFileTreeNode
    folder_list: List[SimpleFileTreeNode]

    def __init__(self):
        super().__init__()
        self.answer_text = "The total size of all small folders is: %d."
        self.bonus_answer_text = "The smallest folder that can be deleted to free enough space has size: %d."
        self.task_number = 7

    def parse_input_to_file_tree(self, input_file_content: List[str]):
        if not input_file_content[0].replace('\n', '') == "$ cd /":
            raise "Can only start a file tree beginning with /"
        self.file_tree = SimpleFileTreeNode('/')
        self.folder_list = [self.file_tree]
        current_node = self.file_tree

        for line in input_file_content[1:]:
            pure_line = line.replace('\n', '')
            if re.fullmatch(valid_res[0], pure_line):  # == ls
                continue  # no useful information in this line
            elif re.fullmatch(valid_res[1], pure_line):  # == cd
                target_node = pure_line.split()[-1]
                if target_node == "/":
                    current_node = self.file_tree
                else:
                    current_node = current_node.traverse(target_node)
                    if current_node not in self.folder_list:
                        self.folder_list.append(current_node)
            elif re.fullmatch(valid_res[2], pure_line):  # == dir
                node = current_node.add_child_node(name=pure_line.split()[-1], is_folder=True)
                if node not in self.folder_list:
                    self.folder_list.append(node)
            elif re.fullmatch(valid_res[3], pure_line):  # == file
                size, name = pure_line.split()
                current_node.add_child_node(name=name, is_folder=False, size=int(size))
            else:
                raise "invalid input detected: %s" % pure_line

    def solve_task(self, input_file_content: List[str]):
        self.parse_input_to_file_tree(input_file_content)
        # self.file_tree.print_files() uncomment if you want to visualize the whole file structure
        return sum([x.size for x in self.folder_list if x.size <= 100000])

    def solve_bonus_task(self, input_file_content: List[str]):
        self.parse_input_to_file_tree(input_file_content)
        total_space = 70000000
        needed_free_space = 30000000
        occupied_space = self.file_tree.size
        folder_to_delete_min_size = needed_free_space - (total_space - occupied_space)
        self.folder_list.sort(key=lambda x: x.size)
        return [x for x in self.folder_list if x.size >= folder_to_delete_min_size][0].size

    def is_input_valid(self, input_file_content: List[str]):
        for line in input_file_content:
            if not any([re.fullmatch(x, line.replace('\n', '')) for x in valid_res]):
                return False
        return True
