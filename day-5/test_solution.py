from solution import Solution


def test_solution_example_part_one():
    solution = Solution()
    assert solution.apply_stacking_instructions_from_file(
        "example_input.txt") == "CMZ"


def test_solution_example_part_two():
    solution = Solution()
    assert solution.apply_stacking_instructions_from_file(
        "example_input.txt", True) == "MCD"


def test_solution_real_input_part_one():
    solution = Solution()
    assert solution.apply_stacking_instructions_from_file(
        "input.txt") == "LJSVLTWQM"


def test_solution_real_input_part_two():
    solution = Solution()
    assert solution.apply_stacking_instructions_from_file(
        "input.txt", True) == "BRQWDBBJM"
