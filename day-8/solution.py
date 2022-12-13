#!/usr/bin/python
"""
Solution to Day 8 of the Advent of Code 2022 event.

https://adventofcode.com/2022/day/8

Usage:
    If using an input file 'solution.py --input-file <input file name>'
    If using text as input 'solution.py --input-text "<input>"'
"""

import argparse


class Solution():
    """
    Class that builds the solution
    """

    def __init__(self):
        self.trees_grid = []
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
            self.process_input(args.input_file)
        elif args.input_text:
            self.process_input(args.input_text, False)
        self.result_part_one = self.get_number_of_visible_trees()
        self.result_part_two = self.find_ideal_view()

    def process_input(self, input_data, is_file=True):
        """
        Reads the input
        """
        if is_file:
            with open(input_data, 'r', encoding='utf-8') as file:
                self.trees_grid = file.read().splitlines()
        else:
            self.trees_grid = input_data.strip().split("\n")

    def get_number_of_visible_trees(self):
        """
        Returns number of visible trees
        """
        count = 0
        for i_row, row_element in enumerate(self.trees_grid):
            for i_col, _ in enumerate(self.trees_grid):
                current = row_element[i_col]
                # check if edge
                if (i_row == 0 or i_row == len(self.trees_grid)-1 or i_col == 0
                        or i_col == len(self.trees_grid[0])-1):
                    count += 1
                # check right
                elif self.check_if_visible_left_right(current, row_element[i_col+1:], "r")[1]:
                    count += 1
                # check left
                elif self.check_if_visible_left_right(current, row_element[:i_col], "l")[1]:
                    count += 1
                # check up
                elif self.check_if_visible_up_down(current, self.trees_grid[:i_row], i_col, "u")[1]:
                    count += 1
                # check down
                elif self.check_if_visible_up_down(current, self.trees_grid[i_row+1:], i_col, "d")[1]:
                    count += 1
        return count

    def check_if_visible_left_right(self, tree, tree_line, direction):
        """
        Returns list, first is number of visible trees, second is if view
            is unobstructed
        """
        visible = 0
        unobstructed = 1
        # if direction left flip treeline so view is outwards
        if direction == "l":
            tree_line = tree_line[::-1]
        for each in tree_line:
            visible += 1
            if tree <= each:
                unobstructed = 0
                break
        return [visible, unobstructed]

    def check_if_visible_up_down(self, tree, tree_line, col, direction):
        """
        Returns list, first is number of visible trees, second is if view
            is unobstructed
        """
        visible = 0
        unobstructed = 1
        # if direction up flip treeline so view is outwards
        if direction == "u":
            tree_line = tree_line[::-1]
        for each in tree_line:
            visible += 1
            if tree <= each[col]:
                unobstructed = 0
                break
        return [visible, unobstructed]

    def find_ideal_view(self):
        """
        Returns the most number of visible trees from a location
        """
        max_score = 0
        for row in range(len(self.trees_grid)):
            for col in range(len(self.trees_grid)):
                # check if edge, it will be a *0 which can be ignored
                if row == 0 or row == len(self.trees_grid)-1 or col == 0 or col == len(self.trees_grid[0])-1:
                    continue
                current = self.trees_grid[row][col]
                total_visible = []
                # check right
                total_visible += [self.check_if_visible_left_right(
                    current, self.trees_grid[row][col+1:], "r")[0]]
                # check left
                total_visible += [self.check_if_visible_left_right(
                    current, self.trees_grid[row][:col], "l")[0]]
                # check up
                total_visible += [self.check_if_visible_up_down(
                    current, self.trees_grid[:row], col, "u")[0]]
                # check down
                total_visible += [self.check_if_visible_up_down(
                    current, self.trees_grid[row+1:], col, "d")[0]]
                score = 1
                for visible in total_visible:
                    score = score * visible
                if score > max_score:
                    max_score = score
        return max_score


if __name__ == "__main__":
    solution = Solution()
    solution.get_arguments()
    print(f"Solution Part One : {solution.result_part_one}")
    print(f"Solution Part Two : {solution.result_part_two}")
