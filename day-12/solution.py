#!/usr/bin/python
"""
Solution to Day 12 of the Advent of Code 2022 event.

https://adventofcode.com/2022/day/11

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
        self.monkeys = []
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
            self.process_file(args.input_file, 20, False)
            self.result_part_one = self.get_level_monkey_business()
            self.process_file(args.input_file, 10000, True)
        elif args.input_text:
            self.process_file(args.input_text, 20, False, False)
            self.result_part_one = self.get_level_monkey_business()
            self.process_file(args.input_text, 10000, True, False)
        self.result_part_two = self.get_level_monkey_business()

    def process_file(self, input_data, number_of_rounds, no_divide, is_file=True):
        """
        Reads the input file
        """
        self.monkeys = []
        if is_file:
            with open(input_data, 'r', encoding="utf-8") as file:
                monkeys = file.read().split("\n\n")
        else:
            monkeys = input_data.split("\n\n")
        for each in monkeys:
            insructions = each.split("\n")
            insructions = [x.split() for x in insructions]
            holding = []
            for item in insructions[1][2:]:
                holding.append(Item(item))
            operation = insructions[2][-2:]
            test = insructions[3][-1]
            on_true = insructions[4][-1]
            on_false = insructions[5][-1]
            monkey = Monkey(holding, operation, test, on_true, on_false)
            self.monkeys.append(monkey)
        # neat trick to keep numbers small, use least common multiple(lcm)
        # eg, divide by lcm and set the remainder as the worry level
        if no_divide:
            no_divide = 1
            for monkey in self.monkeys:
                no_divide = no_divide * int(monkey.test)
        self.run_rounds(number_of_rounds, no_divide)

    def run_rounds(self, number_of_rounds, no_divide):
        """
        This function completes rounds
        """
        for _ in range(number_of_rounds):
            for monkey in self.monkeys:
                for _ in range(len(monkey.holding)):
                    item = monkey.holding[0]
                    throw_to = monkey.take_turn(no_divide)
                    if throw_to:
                        self.monkeys[int(throw_to)].holding.append(item)

    def get_level_monkey_business(self):
        """
        Returns the the level of monkey business.

        Formula: top 2 monkeys by number of inspections, multiplied togther"""
        monkey_business = []
        for monkey in self.monkeys:
            monkey_business.append(monkey.inspections)
        monkey_business = sorted(monkey_business)
        return monkey_business[-1] * monkey_business[-2]


if __name__ == "__main__":
    solution = Solution()
    solution.get_arguments()
    print(f"Solution Part One : {solution.result_part_one}")
    print(f"Solution Part Two : {solution.result_part_two}")
