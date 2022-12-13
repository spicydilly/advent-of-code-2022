#!/usr/bin/python
"""
Solution to Day 1 of the Advent of Code 2022 event.

https://adventofcode.com/2022/day/1

Usage: 
    If using an input file 'solution.py --input-file <input file name>'
    If using text as input 'solution.py --input-text "<input>"'
"""

import argparse


class Solution():
    """
    Class that builds the solution
    """

    def __init__(self):
        self.calories_by_elf = []

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
            self.get_groupings_from_input(args.input_file)
        elif args.input_text:
            self.get_groupings_from_input(args.input_text, False)

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
        for _ in range(3):
            current_max_elf = self.get_max()
            result += [self.calories_by_elf[current_max_elf]]
            self.calories_by_elf.pop(current_max_elf)
        return sum(result)

    def get_groupings_from_input(self, input_data, is_file=True):
        """
        Reads input and returns the total calories consumed
            by each elf
        """
        calories_by_elf = {}
        elf = 0
        input_split = []
        if is_file:
            with open(input_data, 'r', encoding="utf-8") as file:
                input_split = file.read().split("\n\n")
        else:
            input_split = input_data.split("\n\n")
        for grouping in input_split:
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
