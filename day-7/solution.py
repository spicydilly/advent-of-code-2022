#!/usr/bin/python
"""
Solution to Day 7 of the Advent of Code 2022 event.

https://adventofcode.com/2022/day/7

Usage:
    If using an input file 'solution.py --input-file <input file name>'
    If using text as input 'solution.py --input-text "<input>"'
"""

import argparse


class FileSystem():
    """
    Class that fakes a filesystem
    """

    def __init__(self):
        self.file_system = {
            "/": {
                "size": 0,
                "content": dict()
            }
        }
        self.current_dir = ""
        self.path = ""

    def add_file(self, file_name, file_size):
        """
        Adds a file to the filesystem
        """
        self.file_system[self.current_dir]["content"][file_name] = {
            "size": file_size
        }
        self.file_system[self.current_dir]["size"] += int(file_size)
        return True

    def add_directory(self, name):
        """
        Adds a driectory to the filesystem
        """
        self.file_system[self.current_dir + name + "/"] = {
            "content": dict(),
            "size": 0
        }
        return True

    def move_directory(self, target_directory):
        """
        Moves the current directory to the target directory
        """
        if target_directory == "..":
            parent_dir = self.current_dir.split("/")[:-2]
            self.current_dir = "/".join(parent_dir) + "/"
        elif target_directory == "/":
            self.current_dir = "/"
        else:
            self.current_dir += target_directory + "/"

    def get_directory_sizes(self):
        """
        Returns a dictionary of the directories along with their sizes
        """
        dict_dir = {dir: self.file_system[dir] for dir in self.file_system}
        for dir_i in dict_dir:
            dict_dir[dir_i] = self.file_system[dir_i]["size"]
            for dir2 in dict_dir:
                if dir_i == dir2:
                    continue
                if dir_i in dir2:
                    dict_dir[dir_i] += self.file_system[dir2]["size"]
        return dict_dir


class Solution():
    """
    Class that builds the solution
    """

    def __init__(self):
        self.file_system = FileSystem()
        self.result_part_one = 0
        self.result_part_two = 0

    def get_arguments(self):
        """
        Handles the arguments that are available for this class
        """
        parser = argparse.ArgumentParser()
        parser.add_argument("--input-file", type=str, required=False,
                            help="Input file")
        parser.add_argument("--input-text", type=str, required=False,
                            help="Input text")
        args = parser.parse_args()
        if args.input_file:
            self.process_input(args.input_file)
        elif args.input_text:
            self.process_input(args.input_text, False)
        self.result_part_one = self.get_sum_of_directories_that_meet_size(
            100000)
        self.result_part_two = self.smallest_directory_to_delete_to_meet_space(
            70000000, 30000000)

    def process_input(self, input_data, is_file=True):
        """
        Reads the input, returns directory as dictionary
        """
        data = ""
        if is_file:
            with open(input_data, 'r', encoding='utf-8') as file:
                data = file.read()
        else:
            data = input_data
        for line in data.split("\n"):
            if line:
                self.determine_output(line)
        return self.file_system

    def determine_output(self, line):
        """
        Determines the command that was run, to build filesystem
        """
        parsed_line = line.split()
        if parsed_line[0] == "ls":
            return
        elif parsed_line[0] == "$":
            if parsed_line[1] == "cd":
                self.file_system.move_directory(parsed_line[2])
        elif parsed_line[0] == "dir":
            self.file_system.add_directory(parsed_line[1])
        else:
            self.file_system.add_file(parsed_line[1], parsed_line[0])
        return

    def get_sum_of_directories_that_meet_size(self, criteria):
        """
        Returns sum of size of directories that meet criteria size
        """
        sizes = self.file_system.get_directory_sizes()
        result = sum(
            x for x in sizes.values()
            if x <= criteria
        )
        return result

    def smallest_directory_to_delete_to_meet_space(self, capacity, target):
        """
        Returns the smallest directory that, if deleted, would free up 
            enough space to meet target
        """
        used = self.file_system.get_directory_sizes()
        unused = capacity - used["/"]
        smallest_size = capacity
        for directory in used:
            if directory == "/":
                continue
            if used[directory] <= smallest_size and (unused + used[directory]) >= target:
                smallest_size = used[directory]
        return smallest_size


if __name__ == "__main__":
    solution = Solution()
    solution.get_arguments()
    print(f"Solution Part One : {solution.result_part_one}")
    print(f"Solution Part Two : {solution.result_part_two}")
