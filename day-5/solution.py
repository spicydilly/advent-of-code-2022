#!/usr/bin/python
"""
Solution to Day 5 of the Advent of Code 2022 event.

https://adventofcode.com/2022/day/5

Usage   : call with 'solution.py --input <input file name>'
"""

import argparse
from ast import parse


class Solution():

    def get_arguments(self):
        """
        Handles the arguments that are available for this class
        """
        parser = argparse.ArgumentParser()
        parser.add_argument("--input", type=str, required=False,
                            help="Input file")
        self.args = parser.parse_args()
        self.result_part_one = self.apply_stacking_instructions_from_file(
            self.args.input)
        self.result_part_two = self.apply_stacking_instructions_from_file(
            self.args.input, True)

    def apply_stacking_instructions_from_file(self, input_file, multiple=False):
        """
        Reads the input file and returns the new stack layout after stacking
            instructions are completed
        """
        result = None
        with open(input_file, 'r') as f:
            # split by empty newlines in file
            sections = f.read().split("\n\n")
            # first section is initial stack
            self.initial_stack = self.get_the_stack(sections[0].split("\n"))
            instructions = self.get_the_instructions(
                sections[1].split("\n"))
            new_stack = self.complete_instructions(
                instructions, self.initial_stack, multiple)
            result = self.get_top_cases(new_stack)
        return result

    def get_the_stack(self, stack_file_input):
        """
        Returns the stack as a list of lists
        """
        number_of_stacks = int(stack_file_input[-1].split()[-1])
        stacks = [[] for i in range(1, number_of_stacks+1)]
        for line in stack_file_input[:-1]:
            if line:
                stack_number = 0
                for i in range(0, len(line), 4):
                    stacks[stack_number].append(line[i:i+4].strip())
                    stack_number += 1
        return stacks

    def get_the_instructions(self, instruction_file_input):
        """
        Returns instructions as a list of lists

        Format = [ NUMBER TO MOVE, FROM, TO ]
        """
        instructions = []
        for instruction in instruction_file_input:
            if instruction:
                temp_instruction = instruction.split()
                instructions += [[
                    int(temp_instruction[1]),
                    int(temp_instruction[3]),
                    int(temp_instruction[5])
                ]]
        return instructions

    def complete_instructions(self, insructions, the_stack, multiple):
        """
        Returns new stack list, after completing instructions
        """
        for instruction in insructions:
            number_to_move = instruction[0]
            from_location = instruction[1] - 1
            to_location = instruction[2] - 1
            temp_storage = []
            row_number = 0
            for case in the_stack[from_location]:
                if len(temp_storage) == number_to_move:
                    break
                if case:
                    if multiple:
                        temp_storage.append(case)
                    else:
                        temp_storage = [case] + temp_storage
                    the_stack[from_location][row_number] = ""
                row_number += 1
            the_stack[to_location] = self.stack_on_top(
                temp_storage, the_stack[to_location])
        return the_stack

    def stack_on_top(self, to_add, stack):
        """
        Helper function to stack ontop of cases
        """
        temp_stack = list(filter(None, stack))
        return to_add + temp_stack

    def get_top_cases(self, stacks):
        """
        Returns the top cases of the stacks
        """
        result = ""
        for stack in stacks:
            if stack:
                temp_stack = list(filter(None, stack))
                result += temp_stack[0][1]
        return result


if __name__ == "__main__":
    solution = Solution()
    solution.get_arguments()
    print(f"Solution Part One : {solution.result_part_one}")
    print(f"Solution Part Two : {solution.result_part_two}")
