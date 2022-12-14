#!/usr/bin/python
"""
Solution to Day 13 of the Advent of Code 2022 event.

https://adventofcode.com/2022/day/13

Usage:
    If using an input file 'solution.py --input-file <input file name>'
    If using text as input 'solution.py --input-text "<input>"'
"""
from dataclasses import dataclass, field
import argparse
import json


@dataclass
class Pairs:
    """Class that defines the Pairs"""
    packets: list[list] = field(default_factory=list)

    def check_if_in_order(self) -> int:
        """Returns True if packets are in right order"""
        count = 0
        for pairs in range(0, len(self.packets), 2):
            packet_one = self.packets[pairs]
            packet_two = self.packets[pairs+1]
            if self.compare_packets(packet_one, packet_two):
                count += pairs//2 + 1
        return count

    def compare_packets(self, packet_x, packet_y) -> bool:
        """Compares two packets, returns true if x is smaller than y, None if same"""
        for x, y in zip(packet_x, packet_y):
            if isinstance(x, int) and isinstance(y, int):
                if x < y:
                    return True
                if x > y:
                    return False
            elif isinstance(x, list) and isinstance(y, list):
                result = self.compare_packets(x, y)
                if result is not None:
                    return result
            elif isinstance(x, int):  # y must be list
                result = self.compare_packets([x], y)
                if result is not None:
                    return result
            else:  # x must be list, y is int
                result = self.compare_packets(x, [y])
                if result is not None:
                    return result
        if len(packet_x) < len(packet_y):
            return True
        if len(packet_x) > len(packet_y):
            return False
        return None


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

    def indices_of_pairs_in_order(self) -> int:
        """
        Returns the sum of the indices of the pairs that are in right order
        """
        pairs = self.load_pairs()
        return pairs.check_if_in_order()

    def decoder_key(self):
        """Returns the decoder key"""
        pairs = self.load_pairs()
        pairs.packets.append([[2]])
        pairs.packets.append([[6]])
        result = (1 + sum(1 for packet in pairs.packets if pairs.compare_packets(packet, [[2]]) == 1)) * (
            1 + sum(1 for packet in pairs.packets if pairs.compare_packets(packet, [[6]]) == 1))
        return result


if __name__ == "__main__":
    solution = Solution()
    solution.get_arguments()
    print(f"Solution Part One : {solution.result_part_one}")
    print(f"Solution Part Two : {solution.result_part_two}")
