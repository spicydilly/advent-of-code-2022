#!/usr/bin/python
"""
Solution to Day 4 of the Advent of Code 2022 event.

https://adventofcode.com/2022/day/4

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
        self.sections = []
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
            self.get_sections_from_input(args.input_file)
        elif args.input_text:
            self.get_sections_from_input(args.input_text, False)
        self.result_part_one = self.get_overlapping_sections()
        self.result_part_two = self.get_overlapping_sections(True)

    def get_sections_from_input(self, input_data, is_file=True):
        """Proccesses the input"""
        input_split = []
        if is_file:
            with open(input_data, 'r', encoding="utf-8") as file:
                input_split = file.read().split("\n")
        else:
            input_split = input_data.split("\n")
        self.sections = input_split

    def get_overlapping_sections(self, partial=False):
        """
        Reads the input file and returns the number of overlapping
            sections in a file

        Partial is true when we want to just check if there is
            any sort of overlap
        """
        total_overlap = 0
        for pairs in self.sections:
            # split by line, ignoring empty if the value is empty
            if pairs:
                pair = pairs.split(",")
                if partial:
                    total_overlap += self.check_for_partial_overlap(pair)
                else:
                    total_overlap += self.check_for_full_overlap(pair)

        return total_overlap

    def check_for_full_overlap(self, pair):
        """
        Checks for fully overlapping sections in a pair of sections

        Returns 1 if it overlaps, 0 if not
        """
        pair_one_range = [section for section in range(
            int(pair[0].split("-")[0]), int(pair[0].split("-")[1])+1)]
        pair_two_range = [section for section in range(
            int(pair[1].split("-")[0]), int(pair[1].split("-")[1])+1)]
        if (self.full_overlap_helper(pair_one_range, pair_two_range) or
                self.full_overlap_helper(pair_two_range, pair_one_range)):
            return 1
        return 0

    def full_overlap_helper(self, pair_x, pair_y):
        """
        Helper function for check if a full overlap exists
            between two lists of numbers
        """
        for section in pair_x:
            if section not in pair_y:
                return False
        return True

    def check_for_partial_overlap(self, pair):
        """
        Checks for overlapping sections in a pair of sections

        Returns 1 if it overlaps, 0 if not
        """
        pair_one_range = [section for section in range(
            int(pair[0].split("-")[0]), int(pair[0].split("-")[1])+1)]
        pair_two_range = [section for section in range(
            int(pair[1].split("-")[0]), int(pair[1].split("-")[1])+1)]
        if (self.partial_overlap_helper(pair_one_range, pair_two_range) or
                self.partial_overlap_helper(pair_two_range, pair_one_range)):
            return 1
        return 0

    def partial_overlap_helper(self, pair_x, pair_y):
        """
        Helper function for check if a partial overlap exists
            between two lists of numbers
        """
        for section in pair_x:
            if section in pair_y:
                return True
        return False


if __name__ == "__main__":
    solution = Solution()
    solution.get_arguments()
    print(f"Solution Part One : {solution.result_part_one}")
    print(f"Solution Part Two : {solution.result_part_two}")
