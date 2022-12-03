#!/usr/bin/python
"""
Solution to Day 2 of the Advent of Code 2022 event.

https://adventofcode.com/2022/day/2

Usage   : call with 'solution.py --input <input file name>'
"""

import argparse
from ast import parse


class Solution():

    SCORING_CHOICE = {"X": 1, "Y": 2, "Z": 3}
    SCORING_RESULT = {
        "A": {"X": 3, "Y": 6, "Z": 0},
        "B": {"X": 0, "Y": 3, "Z": 6},
        "C": {"X": 6, "Y": 0, "Z": 3}
    }
    STRATEGY_RESULT = {
        "X": {"A": "Z", "B": "X", "C": "Y"},
        "Y": {"A": "X", "B": "Y", "C": "Z"},
        "Z": {"A": "Y", "B": "Z", "C": "X"}
    }

    def get_arguments(self):
        """
        Handles the arguments that are available for this class
        """
        parser = argparse.ArgumentParser()
        parser.add_argument("--input", type=str, required=False,
                            help="Input file")
        self.args = parser.parse_args()
        self.result_part_one = self.get_scoring_from_file(
            self.args.input)
        self.result_part_two = self.get_scoring_from_file(
            self.args.input, True)

    def get_scoring_from_file(self, input_file, use_strategy=False):
        """
        Reads the input file and returns the score of the player
        """
        score = 0
        with open(input_file, 'r') as f:
            for round in f.read().split("\n"):
                # split by line, ignoring empty if the value is empty
                if round:
                    opponent, mine = round.split()
                    if use_strategy:
                        score += self.determine_score_when_strategy(
                            opponent, mine)
                    else:
                        score += self.determine_score_player_input(
                            opponent, mine)

        return score

    def determine_score_player_input(self, opponent, mine):
        """
        Returns score of each round, when 'mine' is the players choice

        Score is determined by:
            3 points for draw;
            6 points for win;
            +
            the points for the 'mine' choice, stored in SCORING_SYSTEM

        Notes:
            A:X; Rock
            B:Y; Paper
            C:Z; Scissors
        """
        return self.SCORING_RESULT[opponent][mine] + self.SCORING_CHOICE[mine]

    def determine_score_when_strategy(self, opponent, mine):
        """
        Returns score of each round, when strategy is specified

        Notes:
            X; Lose
            Y: Draw
            Z: Win
        """
        return self.determine_score_player_input(opponent, self.STRATEGY_RESULT[mine][opponent])


if __name__ == "__main__":
    solution = Solution()
    solution.get_arguments()
    print(f"Solution Part One : {solution.result_part_one}")
    print(f"Solution Part Two : {solution.result_part_two}")
