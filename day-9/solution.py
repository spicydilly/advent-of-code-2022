#!/usr/bin/python
"""
Solution to Day 9 of the Advent of Code 2022 event.

https://adventofcode.com/2022/day/9

Usage   : call with 'solution.py --input <input file name>'
"""

import argparse
import numpy as np


class Knot():
    """
    Class that defines a knot
    """

    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def __sub__(self, knot):
        """
        Subtracting a knot, provides the distance
        """
        return Knot(self.pos_x - knot.pos_x, self.pos_y - knot.pos_y)

    def normalize(self):
        """
        Returns normalized pos_x y
        """
        return np.linalg.norm([self.pos_x, self.pos_y])


class Solution():
    """
    Class that builds the solution
    """

    def __init__(self):
        self.last_knot_trail = []
        self.rope = []
        self.number_of_knots = 2
        self.result_part_one = 0
        self.result_part_two = 0

    def get_arguments(self):
        """
        Handles the arguments that are available for this class
        """
        parser = argparse.ArgumentParser()
        parser.add_argument("--input", type=str, required=True,
                            help="Input file")
        args = parser.parse_args()
        self.process_file(args.input, 2)
        self.result_part_one = self.number_of_locations_visited_by_last_knot()
        self.process_file(args.input, 10)
        self.result_part_two = self.number_of_locations_visited_by_last_knot()

    def process_file(self, input_file, number_of_knots):
        """
        Reads the input file, returns directory as dictionary
        """
        self.number_of_knots = number_of_knots
        self.rope = [
            Knot(0, 0)
            for i in range(number_of_knots)
        ]
        self.last_knot_trail = {
            (
                self.rope[number_of_knots-1].pos_x,
                self.rope[number_of_knots-1].pos_y
            )
        }
        with open(input_file, 'r', encoding="utf-8") as f:
            all_instructions = f.read().splitlines()
            for instruction in all_instructions:
                if instruction:
                    self.rope = self.determine_movement(
                        self.rope, instruction.split())
        return self.rope

    def determine_movement(self, rope, instruction):
        """
        Determines the move to take
        """
        direction = instruction[0]
        amount = int(instruction[1])
        for _ in range(1, int(amount)+1):
            match direction:
                case "R":
                    rope[0].pos_x += 1
                case "L":
                    rope[0].pos_x -= 1
                case "U":
                    rope[0].pos_y += 1
                case "D":
                    rope[0].pos_y -= 1
            for knot in range(self.number_of_knots-1):
                if (rope[knot] - rope[knot+1]).normalize() >= 2:
                    rope[knot+1].pos_x += (rope[knot+1].pos_x != rope[knot].pos_x) * \
                        np.sign(rope[knot].pos_x - rope[knot+1].pos_x)
                    rope[knot+1].pos_y += (rope[knot+1].pos_y != rope[knot].pos_y) * \
                        np.sign(rope[knot].pos_y - rope[knot+1].pos_y)
                    if knot+1 == self.number_of_knots-1:
                        self.last_knot_trail.add(
                            (rope[knot+1].pos_x, rope[knot+1].pos_y))
        return rope

    def number_of_locations_visited_by_last_knot(self):
        """
        Returns number of locations that were visited once
        """
        return len(self.last_knot_trail)


if __name__ == "__main__":
    solution = Solution()
    solution.get_arguments()
    print(f"Solution Part One : {solution.result_part_one}")
    print(f"Solution Part Two : {solution.result_part_two}")
