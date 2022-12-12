#!/usr/bin/python
"""
Solution to Day 10 of the Advent of Code 2022 event.

https://adventofcode.com/2022/day/10

Usage:
    If using an input file 'solution.py --input-file <input file name>'
    If using text as input 'solution.py --input-text "<input>"'
"""

import argparse
import numpy as np


class Executor():
    """
    Class that defines the executor/CPU
    """

    def __init__(self):
        self.cycle = [0, 1]  # cycle number, value
        self.monitor = []
        self.mointor_cycle_number = 20
        self.crt = []

    def cycle_add_value(self, value):
        """
        Increases the value
        """
        self.cycle[1] += int(value)

    def cycle_increment(self):
        """
        Increase the cycle number
        """
        self.cycle[0] += 1
        self.cycle_monitor()

    def cycle_monitor(self):
        """
        Checks if the current cycle should be monitored, and adds pixel
            to monitor.
        """
        pixel = "."
        sprite_position = [
            self.cycle[1]-1,
            self.cycle[1],
            self.cycle[1]+1
        ]
        crt_row = self.cycle[0] - (((self.cycle[0]-1) // 40) * 40) - 1
        if crt_row in sprite_position:
            pixel = "#"
        self.crt.append(pixel)
        if self.cycle[0] == self.mointor_cycle_number:
            self.monitor.append(self.cycle[0] * self.cycle[1])
            self.mointor_cycle_number += 40


class Solution():
    """
    Class that builds the solution
    """

    def __init__(self):
        self.executor = Executor()
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
            self.process_file(args.input_file)
        elif args.input_text:
            self.process_file(args.input_text, False)
        self.result_part_one = self.sum_signal_monitor()
        self.result_part_two = self.get_crt()

    def process_file(self, input_data, is_file=True):
        """
        Reads the input file
        """
        if is_file:
            with open(input_data, 'r', encoding="utf-8") as file:
                all_instructions = file.read().splitlines()
        else:
            all_instructions = input_data.split("\n")
        for instruction in all_instructions:
            if instruction:
                instruction = instruction.split()
                self.executor.cycle_increment()
                if instruction[0] == "addx":
                    self.executor.cycle_increment()
                    self.executor.cycle_add_value(instruction[1])

    def sum_signal_monitor(self):
        """
        Returns the sum of the signal strengths that are monitored
        """
        return sum(self.executor.monitor)

    def get_crt(self):
        """
        Retruns the formatted CRT screen, in 6 rows of 40
        """
        crt_array = np.array_split(self.executor.crt, 6)
        crt = ""
        for row in crt_array:
            crt += "\n" + "".join(row)
        return crt


if __name__ == "__main__":
    solution = Solution()
    solution.get_arguments()
    print(f"Solution Part One : {solution.result_part_one}")
    print(f"Solution Part Two : {solution.result_part_two}")
