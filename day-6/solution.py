#!/usr/bin/python
"""
Solution to Day 6 of the Advent of Code 2022 event.

https://adventofcode.com/2022/day/6

Usage   : call with 'solution.py --input <input file name>'
"""

import argparse


class Solution():
    """
    Class that builds the solution
    """

    def __init__(self):
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
            self.result_part_one = self.process_file(args.input_file, 4)
            self.result_part_two = self.process_file(args.input_file, 14)
        elif args.input_text:
            self.result_part_one = self.process_file(args.input_text, 4, False)
            self.result_part_two = self.process_file(
                args.input_text, 14, False)

    def process_file(self, input_data, marker_size, is_file=True):
        """
        Reads the input and returns the number of characters
            that needed to be processes before the first start-of-packet
            marker is detected
        """
        result = None
        data = ""
        if is_file:
            with open(input_data, 'r', encoding='utf-8') as file:
                data = file.read()
        else:
            data = input_data
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
