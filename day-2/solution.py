#!/usr/bin/python
"""
Solution to Day 2 of the Advent of Code 2022 event.

https://adventofcode.com/2022/day/2

Usage: 
    If using an input file 'solution.py --input-file <input file name>'
    If using text as input 'solution.py --input-text "<input>"'
"""

import argparse


class Solution():
    """
    Class that builds the solution
    """

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
        scoring = [0, 0]
        if args.input_file:
            scoring = self.get_scoring_from_input(
                args.input_file)
        elif args.input_text:
            scoring = self.get_scoring_from_input(
                args.input_text, False)
        self.result_part_one = scoring[0]
        self.result_part_two = scoring[1]

    def get_scoring_from_input(self, input_data, is_file=True):
        """
        Reads the input and returns the score of the player

        Score in format [<no strategy>, <strategy>]
        """
        score = [0, 0]
        input_split = []
        if is_file:
            with open(input_data, 'r', encoding="utf-8") as file:
                input_split = file.read().split("\n")
        else:
            input_split = input_data.split("\n")
        for round_number in input_split:
            # split by line, ignoring empty if the value is empty
            if round_number:
                opponent, mine = round_number.split()
                score[1] += self.determine_score_when_strategy(
                    opponent, mine)
                score[0] += self.determine_score_player_input(
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
