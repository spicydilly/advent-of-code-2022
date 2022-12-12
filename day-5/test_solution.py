from solution import Solution


def test_solution_example_part_one():
    solution = Solution()
    solution.process_input("example_input.txt")
    assert solution.apply_stacking_instructions() == "CMZ"


def test_solution_example_part_two():
    solution = Solution()
    solution.process_input("example_input.txt")
    assert solution.apply_stacking_instructions(True) == "MCD"


def test_solution_real_input_part_one():
    solution = Solution()
    solution.process_input("input.txt")
    assert solution.apply_stacking_instructions() == "LJSVLTWQM"


def test_solution_real_input_part_two():
    solution = Solution()
    solution.process_input("input.txt")
    assert solution.apply_stacking_instructions(True) == "BRQWDBBJM"
