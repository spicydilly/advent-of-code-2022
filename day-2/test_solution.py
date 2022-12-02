from solution import Solution


def test_solution_example_part_one():
    solution = Solution()
    assert solution.get_scoring_from_file("example_input.txt") == 15


def test_solution_example_part_two():
    solution = Solution()
    assert solution.get_scoring_from_file("example_input.txt", True) == 12


def test_solution_real_input_part_one():
    solution = Solution()
    assert solution.get_scoring_from_file("input.txt") == 9651


def test_solution_real_input_part_two():
    solution = Solution()
    assert solution.get_scoring_from_file("input.txt", True) == 10560
