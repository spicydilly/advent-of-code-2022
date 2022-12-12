#!/usr/bin/python
"""
Solution to Day 3 of the Advent of Code 2022 event.

https://adventofcode.com/2022/day/3

Usage: 
    If using an input file 'solution.py --input-file <input file name>'
    If using text as input 'solution.py --input-text "<input>"'
"""

import argparse
import string


class Solution():
    """
    Class that builds the solution
    """

    PRIORITIES = dict(zip(string.ascii_letters, range(1, 53)))

    def __init__(self):
        self.rucksacks = []
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
            self.get_rucksacks_from_input(args.input_file)
        elif args.input_text:
            self.get_rucksacks_from_input(args.input_text, False)
        self.result_part_one = self.get_priorities()
        self.result_part_two = self.get_group_badge()

    def get_rucksacks_from_input(self, input_data, is_file=True):
        """Proccesses the input"""
        input_split = []
        if is_file:
            with open(input_data, 'r', encoding="utf-8") as file:
                input_split = file.read().split("\n")
        else:
            input_split = input_data.split("\n")
        self.rucksacks = input_split

    def get_priorities(self):
        """
        Loops rucksacks and returns the sum of priorities
            of items that occur in both compartments of a rucksack
        """
        items = dict.fromkeys(string.ascii_letters, 0)
        for rucksack in self.rucksacks:
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

    def get_group_badge(self):
        """
        Loops rucksacks and returns the sum of the priorities
            of all the badge groups
        """
        items = dict.fromkeys(string.ascii_letters, 0)
        line_count = 0
        group = ""
        for rucksack in self.rucksacks:
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
