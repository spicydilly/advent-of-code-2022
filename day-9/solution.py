#!/usr/bin/python
"""
Solution to Day 9 of the Advent of Code 2022 event.

https://adventofcode.com/2022/day/9

Usage   : call with 'solution.py --input <input file name>'
"""

import argparse
from ast import parse


class Solution():

    def __init__(self):
        self.closest_tail_path = [[0, 0]]
        # [x, y]
        self.head_location = [0, 0]
        self.tail_location = [0, 0]

    def get_arguments(self):
        """
        Handles the arguments that are available for this class
        """
        parser = argparse.ArgumentParser()
        parser.add_argument("--input", type=str, required=True,
                            help="Input file")
        parser.add_argument("--knots", type=str, required=True,
                            help="Number of knots")
        self.args = parser.parse_args()
        self.process_file(self.args.input, self.args.knots)
        self.result_part_one = self.number_of_locations_visited_once()
        self.result_part_two = self.number_of_locations_visited_once(False)

    def process_file(self, input_file, knots):
        """
        Reads the input file, returns directory as dictionary
        """
        head_location = self.head_location
        tail_locations = [self.tail_location * knots]
        with open(input_file, 'r') as f:
            all_instructions = f.read().splitlines()
            for instruction in all_instructions:
                if instruction:
                    head_location, tail_locations = self.determine_movement(
                        head_location, tail_locations, instruction.split())
        return

    def determine_movement(self, head_location, tail_locations, instruction):
        """
        Determines the move to take
        """
        move = instruction[0]
        amount = instruction[1]
        if move == "R":
            head_location, tail_locations = self.move_head(
                0, 1, head_location, tail_locations, amount)
        elif move == "L":
            head_location, tail_locations = self.move_head(
                0, -1, head_location, tail_locations, amount)
        elif move == "U":
            head_location, tail_locations = self.move_head(
                1, 1, head_location, tail_locations, amount)
        elif move == "D":
            head_location, tail_locations = self.move_head(
                1, -1, head_location, tail_locations, amount)
        return head_location, tail_locations

    def move_head(self, direction, step, head_location, tail_locations, amount):
        """
        Moves the head by amount, and checks for tail updates each step

        direction: 0 for x, 1 for y
        """
        for each in range(int(amount)):
            old_head_location = head_location.copy()
            head_location[direction] += step
            tail_locations = self.determine_tail_movement(
                head_location, tail_locations, old_head_location)
            # keep copy of visit
            self.closest_tail_path += [tail_locations.copy()]
        return head_location, tail_locations

    def determine_tail_movement(self, head_location, tail_locations, old_head_location):
        """
        Determines where the tail should move after the head has moved
        """
        for knot in range(tail_locations):
            # check for overlap
            if head_location == tail_locations[knot]:
                return tail_locations[knot]
            x_difference = head_location[0] - tail_locations[knot][0]
            y_difference = head_location[1] - tail_locations[knot][1]
            # check if head x is more than 1 step away than tail x
            if (x_difference > 1) or (x_difference < -1):
                # check if head y is same as tail y
                if head_location[1] == tail_locations[knot][1]:
                    # move in direction of x
                    tail_locations[knot] = [
                        tail_locations[knot][0] + (x_difference/2),
                        tail_locations[knot][1]
                    ]
                else:
                    # move in direction of y
                    tail_locations[knot] = old_head_location
            # check if head y is more than 1 step away than tail y
            elif (y_difference > 1) or (y_difference < -1):
                # check if head y is same as tail y
                if head_location[1] == tail_locations[knot][1]:
                    # move in direction of x
                    tail_locations[knot] = [
                        tail_locations[knot][0],
                        tail_locations[knot][1] + (y_difference/2)
                    ]
                else:
                    # move in direction of y
                    tail_locations[knot] = old_head_location
        return tail_locations

    def number_of_locations_visited_once(self, closest=True):
        """
        Returns number of locations that were visited once
        """
        unique_visits = []
        tail_locations = self.furthest_tail_path
        if closest:
            tail_locations = self.closest_tail_path
        for visit in tail_locations:
            if visit in unique_visits:
                continue
            unique_visits += [visit]
        return len(unique_visits)


if __name__ == "__main__":
    solution = Solution()
    solution.get_arguments()
    print(f"Solution Part One : {solution.result_part_one}")
    print(f"Solution Part Two : {solution.result_part_two}")
