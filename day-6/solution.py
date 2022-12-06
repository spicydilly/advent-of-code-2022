#!/usr/bin/python
"""
Solution to Day 6 of the Advent of Code 2022 event.

https://adventofcode.com/2022/day/6

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
        self.result_part_one = self.process_file(
            self.args.input, 4)
        self.result_part_two = self.process_file(
            self.args.input, 14)

    def process_file(self, input_file, marker_size):
        """
        Reads the input file and returns the number of characters
            that needed to be processes before the first start-of-packet
            marker is detected
        """
        result = None
        with open(input_file, 'r') as f:
            data = f.read()
            result = self.get_start_of_packet(data, marker_size)[0]
        return result

    def get_start_of_packet(self, data, marker_size):
        """
        Returns the start of packet character in the format
            [location, character_that_compeletes_marker]
        """
        for i in range(0, len(data)):
            data_chunk = data[i:i+marker_size]
            if self.check_if_data_chunk_is_unique(data_chunk):
                return [i+marker_size, data_chunk[:-1]]
        return None

    def check_if_data_chunk_is_unique(self, data_chunk):
        """
        Returns true if all characters in a data_chunk are unique
        """
        for entry in data_chunk:
            if data_chunk.count(entry) != 1:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    solution.get_arguments()
    print(f"Solution Part One : {solution.result_part_one}")
    print(f"Solution Part Two : {solution.result_part_two}")
