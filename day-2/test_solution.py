from solution import Solution


def test_solution_example_part_one():
    solution = Solution()
    assert solution.get_scoring_from_input("example_input.txt")[0] == 15


def test_solution_example_part_two():
    solution = Solution()
    assert solution.get_scoring_from_input("example_input.txt", True)[1] == 12


def test_solution_real_input_part_one():
    solution = Solution()
    assert solution.get_scoring_from_input("input.txt")[0] == 9651


def test_solution_real_input_part_two():
    solution = Solution()
    assert solution.get_scoring_from_input("input.txt", True)[1] == 10560
