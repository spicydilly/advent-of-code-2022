#!/usr/bin/python
"""
Solution to Day 1 of the Advent of Code 2022 event.

https://adventofcode.com/2022/day/1

Usage   : call with 'solution.py --input <input file name>'
"""

import argparse
from ast import parse


class Solution():

    def get_arguments(self):
        """
        Handles the arguments that are available for this class
        """
        parser = argparse.ArgumentParser()
        parser.add_argument("--input", type=str, required=False,
                            help="Input file")
        self.args = parser.parse_args()
        self.get_groupings_from_file(self.args.input)

    def get_max(self):
        """
        Returns the elf with the largest amount of calories
        """
        return max(self.calories_by_elf, key=self.calories_by_elf.get)

    def get_top_elf(self):
        return self.calories_by_elf[self.get_max()]

    def get_top_three_elves(self):
        """
        Returns the sum of the top 3 largest amount of calories
        """
        result = []
        for elf in range(3):
            current_max_elf = self.get_max()
            result += [self.calories_by_elf[current_max_elf]]
            self.calories_by_elf.pop(current_max_elf)
        return sum(result)

    def get_groupings_from_file(self, input_file):
        """
        Reads the input file and returns the total calories consumed
            by each elf
        """
        calories_by_elf = {}
        elf = 0
        with open(input_file, 'r') as f:
            # split by empty newlines in file
            for grouping in f.read().split("\n\n"):
                # split by line, ignoring empty if the value is empty
                calories = list(filter(None, grouping.split("\n")))
                # convert the list values to integers
                calories = map(int, calories)
                calories_by_elf[elf] = sum(calories)
                elf += 1
        self.calories_by_elf = calories_by_elf
        return


if __name__ == "__main__":
    solution = Solution()
    solution.get_arguments()
    print(f"Solution Part One : {solution.get_top_elf()}")
    print(f"Solution Part Two: {solution.get_top_three_elves()}")
