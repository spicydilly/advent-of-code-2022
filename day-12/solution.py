#!/usr/bin/python
"""
Solution to Day 12 of the Advent of Code 2022 event.

https://adventofcode.com/2022/day/12

Usage:
    If using an input file 'solution.py --input-file <input file name>'
    If using text as input 'solution.py --input-text "<input>"'
"""
from dataclasses import dataclass, field
from itertools import product
import argparse
import string


@dataclass
class Location:
    """Class that defines the location of a hill"""
    x: int
    y: int


@dataclass
class Hill:
    """Class that defines a Hill"""
    height: int
    visited: bool = False
    climb_cost: int = None


@dataclass
class HeightMap:
    """Class that defines the HeightMap"""
    start: Location = None
    end: Location = None
    hills: list[list[Hill]] = field(default_factory=list)

    def neighbors(self, location: Location) -> Location:
        """Returns neighbors of the location that can be climbed"""
        limit = self.hills[location.y][location.x].height + 1
        possible_moves = [
            Location(x, y) for (x, y) in [
                (location.x - 1, location.y), (location.x + 1, location.y),
                (location.x, location.y - 1), (location.x, location.y + 1)
            ] if 0 <= x < len(self.hills[0]) and 0 <= y < len(self.hills)
        ]
        for neighbor in possible_moves:
            if self.neighbor_location(neighbor).height <= limit:
                yield neighbor

    def neighbor_location(self, location: Location) -> Location:
        """Returns Location object of neighbor"""
        return self.hills[location.y][location.x]

    def traverse(self, queue: list[tuple[int, Location, Location]] = None) -> None:
        """Move along locations"""
        if not queue:
            queue = [(0, self.start, self.start)]
        while queue:
            curr_cost, curr_point, _ = queue.pop(0)
            if not self.neighbor_location(curr_point).visited:
                self.neighbor_location(curr_point).climb_cost = curr_cost
                self.neighbor_location(curr_point).visited = True
                if curr_point == self.end:
                    break
                curr_cost += 1
                for next_location in self.neighbors(curr_point):
                    queue.append((curr_cost, next_location, curr_point))
                queue.sort(key=lambda l: l[0])


@dataclass()
class Solution():
    """
    Class that builds the solution
    """

    map_values: dict[str, int] = field(default_factory=lambda: dict(
        zip(string.ascii_lowercase, range(1, 27))))
    input_data: list = field(default_factory=list)
    result_part_one: int = 0
    result_part_two: int = 0

    def get_arguments(self) -> None:
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
            self.process_input(args.input_file)
        elif args.input_text:
            self.process_input(args.input_text, False)
        self.result_part_one = self.traverse_start_to_end()
        self.result_part_two = self.traverse_each_a_to_end()

    def process_input(self, input_data, is_file=True) -> None:
        """
        Reads the input file
        """
        if is_file:
            with open(input_data, 'r', encoding="utf-8") as file:
                self.input_data = file.read().splitlines()
        else:
            self.input_data = input_data.splitlines()

    def load_map(self) -> HeightMap:
        """Load map from input_data"""
        height_map = HeightMap()
        for row in self.input_data:
            height_map.hills.append([])
            for hill in row:
                if hill == "S":
                    height_map.start = Location(
                        x=len(height_map.hills[-1]),
                        y=len(height_map.hills) - 1
                    )
                    hill = "a"
                elif hill == "E":
                    height_map.end = Location(
                        x=len(height_map.hills[-1]),
                        y=len(height_map.hills) - 1
                    )
                    hill = "z"
                height_map.hills[-1].append(
                    Hill(self.map_values[hill]))
        return height_map

    def traverse_start_to_end(self) -> int:
        """Traverse the map from start to end, return total climbs"""
        map_data = self.load_map()
        map_data.traverse()
        return map_data.neighbor_location(map_data.end).climb_cost

    def traverse_each_a_to_end(self) -> int:
        """Traverse the map from all 'a' locations to end, return total climbs"""
        map_data = self.load_map()
        queue = []
        for (x, y) in product(range(len(map_data.hills[0])), range(len(map_data.hills))):
            coord = Location(x, y)
            if map_data.neighbor_location(coord).height == 1:
                queue.append((0, coord, coord))
        map_data.traverse(queue)
        return map_data.neighbor_location(map_data.end).climb_cost


if __name__ == "__main__":
    solution = Solution()
    solution.get_arguments()
    print(f"Solution Part One : {solution.result_part_one}")
    print(f"Solution Part Two : {solution.result_part_two}")
