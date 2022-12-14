#!/usr/bin/python
"""
Solution to Day 14 of the Advent of Code 2022 event.

https://adventofcode.com/2022/day/13

Usage:
    If using an input file 'solution.py --input-file <input file name>'
    If using text as input 'solution.py --input-text "<input>"'
"""
from dataclasses import dataclass, field
import argparse


@dataclass()
class Solution():
    """Class that builds the solution"""

    input_data: list = field(default_factory=list)
    result_part_one: int = 0
    result_part_two: int = 0

    def get_arguments(self) -> None:
        """Handles the arguments that are available for this class"""
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
        self.result_part_one = self.indices_of_pairs_in_order()
        self.result_part_two = self.decoder_key()

    def process_input(self, input_data, is_file=True) -> None:
        """Reads the input file"""
        if is_file:
            with open(input_data, 'r', encoding="utf-8") as file:
                self.input_data = file.read().split("\n\n")
        else:
            self.input_data = input_data.split("\n\n")

    def load_pairs(self) -> Pairs:
        """Load pairs from input_data"""
        pairs = Pairs()
        for pair in self.input_data:
            split_row = pair.split()
            for packet in split_row:
                pairs.packets.append(json.loads(packet))
        return pairs


if __name__ == "__main__":
    solution = Solution()
    solution.get_arguments()
    print(f"Solution Part One : {solution.result_part_one}")
    print(f"Solution Part Two : {solution.result_part_two}")
