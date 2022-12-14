#!/usr/bin/python
"""
Solution to Day 14 of the Advent of Code 2022 event.

https://adventofcode.com/2022/day/14

Usage:
    If using an input file 'solution.py --input-file <input file name>'
    If using text as input 'solution.py --input-text "<input>"'
"""
from dataclasses import dataclass, field
import argparse


@dataclass
class Reservoir():
    """Class that defines the reservoir"""
    contents: dict[tuple, str] = field(default_factory=dict)

    def drop_sand(self) -> bool:
        """Drop sand into reservoir"""
        drop_x = 500
        drop_y = max(y for (x, y) in self.contents)
        for y in range(drop_y):
            if (drop_x, y + 1) not in self.contents:
                continue
            if (drop_x - 1, y + 1) not in self.contents:
                drop_x -= 1
            elif (drop_x + 1, y + 1) not in self.contents:
                drop_x += 1
            else:
                self.contents[(drop_x, y)] = "o"
                if (drop_x, y) != (500, 0):
                    return True
                return False
        return False

    def add_floor(self):
        """Adds a floor to the contents"""
        drop_y = max(y for (x, y) in self.contents) + 2
        for drop_x in range(-800, 801):  # could be increased
            self.contents[(drop_x, drop_y)] = "#"


@dataclass
class Solution():
    """Class that builds the solution"""

    input_data: list = field(default_factory=list)
    reservoir: dict[tuple, str] = field(default_factory=dict)
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
        self.result_part_one = self.drop_sand_until_abyss()
        self.result_part_two = self.drop_sand_until_floor()

    def process_input(self, input_data, is_file=True) -> None:
        """Reads the input file"""
        if is_file:
            with open(input_data, 'r', encoding="utf-8") as file:
                self.input_data = file.read().splitlines()
        else:
            self.input_data = input_data.splitlines()

    def load_reservoir(self) -> Reservoir:
        """Load reservoir from input_data"""
        reservoir = Reservoir()
        for line in self.input_data:
            path = [point.split(",") for point in line.split("->")]
            points = [(int(point[0]), int(point[1])) for point in path]

            for point_1, point_2 in zip(points, points[1:]):
                x1, y1 = point_1
                x2, y2 = point_2

                for x in range(min(x1, x2), max(x1, x2) + 1):
                    reservoir.contents[(x, y1)] = "#"
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    reservoir.contents[(x1, y)] = "#"
        return reservoir

    def drop_sand_until_abyss(self) -> int:
        """
        Resturns the number of sand dropped into the reservoir until
            it reaches the abyss
        """
        reservoir = self.load_reservoir()
        return self.drop_until_end(reservoir)

    def drop_until_end(self, reservoir) -> int:
        """Return number of sand dropped until it reaches the end"""
        dropped_number = 0
        while reservoir.drop_sand():
            dropped_number += 1
        return dropped_number

    def drop_sand_until_floor(self) -> int:
        """
        Resturns the number of sand dropped into the reservoir until
            it reaches the floor
        """
        reservoir = self.load_reservoir()
        reservoir.add_floor()
        return self.drop_until_end(reservoir) + 1


if __name__ == "__main__":
    solution = Solution()
    solution.get_arguments()
    print(f"Solution Part One : {solution.result_part_one}")
    print(f"Solution Part Two : {solution.result_part_two}")
