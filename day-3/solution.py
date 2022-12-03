#!/usr/bin/python
"""
Solution to Day 3 of the Advent of Code 2022 event.

https://adventofcode.com/2022/day/3

Usage   : call with 'solution.py --input <input file name>'
"""

import argparse
from ast import parse
import string


class Solution():

    PRIORITIES = dict(zip(string.ascii_letters, range(1, 53)))

    def get_arguments(self):
        """
        Handles the arguments that are available for this class
        """
        parser = argparse.ArgumentParser()
        parser.add_argument("--input", type=str, required=False,
                            help="Input file")
        self.args = parser.parse_args()
        self.result_part_one = self.get_priorities_from_file(
            self.args.input)
        self.result_part_two = self.get_group_badge_from_file(
            self.args.input)

    def get_priorities_from_file(self, input_file):
        """
        Reads the input file and returns the sum of priorities
            of items that occur in both compartments of a rucksack
        """
        items = dict.fromkeys(string.ascii_letters, 0)
        with open(input_file, 'r') as f:
            # split by empty newlines in file
            for rucksack in f.read().split("\n"):
                # split by line, ignoring empty if the value is empty
                if rucksack:
                    items = self.combine_pirorities_dict_helper(
                        items,
                        self.find_items_in_both_compartments(rucksack)
                    )

        return sum(items.values())

    def find_items_in_both_compartments(self, rucksack):
        """
        Returns items that are found in both compartments of a rucksack
        """
        compartment_one, compartment_two = rucksack[:len(
            rucksack)//2], rucksack[len(rucksack)//2:]
        both_compartments = {}
        for item in compartment_one:
            if item in compartment_two:
                both_compartments[item] = self.PRIORITIES[item]

        return both_compartments

    def combine_pirorities_dict_helper(self, items, add_priorities):
        """
        Helper method for incrementing the total priorities of items
        """
        for each in add_priorities:
            items[each] += self.PRIORITIES[each]

        return items

    def get_group_badge_from_file(self, input_file):
        """
        Reads the input file and returns the sum of the priorities
            of all the badge groups
        """
        items = dict.fromkeys(string.ascii_letters, 0)
        with open(input_file, 'r') as f:
            line_count = 0
            group = ""
            for rucksack in f.read().split("\n"):
                # split by line, ignoring empty if the value is empty
                if rucksack:
                    line_count += 1
                    group += rucksack + " "
                    if line_count == 3:
                        items = self.combine_pirorities_dict_helper(
                            items,
                            self.find_common_items_in_group(group)
                        )
                        group = ""
                        line_count = 0

        return sum(items.values())

    def find_common_items_in_group(self, rucksacks):
        """
        Returns the common item found in rucksacks
        """
        rucksack = rucksacks.split()
        for item in rucksack[0]:
            if item in rucksack[1] and item in rucksack[2]:
                return item


if __name__ == "__main__":
    solution = Solution()
    solution.get_arguments()
    print(f"Solution Part One : {solution.result_part_one}")
    print(f"Solution Part Two : {solution.result_part_two}")
