#!/usr/bin/python
"""
Solution to Day 1 of the Advent of Code 2022 event. 

https://adventofcode.com/2022/day/1

Usage   : call with 'solution.py --input <input file name>'
Returns : the max amount of calories consumed by an elf
"""

import argparse
from ast import parse


class Solution():

    def __init__(self):
        self.get_arguments()
        self.result = self.get_solution()

    def get_arguments(self):
        """
        Handles the arguments that are available for this class
        """
        parser = argparse.ArgumentParser()
        parser.add_argument("--input", type=str, required=False,
                            help="Input file")
        self.args = parser.parse_args()

    def get_solution(self):
        """
        Returns the largest amount of calories
        """
        calories_by_elf = self.get_groupings_from_file(self.args.input)
        return max(calories_by_elf.values())

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
        return calories_by_elf


if __name__ == "__main__":
    solution = Solution()
    print(solution.result)
