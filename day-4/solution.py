#!/usr/bin/python
"""
Solution to Day 4 of the Advent of Code 2022 event.

https://adventofcode.com/2022/day/4

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
        self.result_part_one = self.get_overlapping_sections_from_file(
            self.args.input)
        self.result_part_two = self.get_overlapping_sections_from_file(
            self.args.input, True)

    def get_overlapping_sections_from_file(self, input_file, partial=False):
        """
        Reads the input file and returns the number of overlapping
            sections in a file

        Partial is true when we want to just check if there is
            any sort of overlap
        """
        total_overlap = 0
        with open(input_file, 'r') as f:
            for pairs in f.read().split("\n"):
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
