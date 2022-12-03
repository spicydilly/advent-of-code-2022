from solution import Solution


def test_solution_example_part_one():
    solution = Solution()
    assert solution.get_priorities_from_file("example_input.txt") == 157


def test_solution_example_part_two():
    solution = Solution()
    assert solution.get_group_badge_from_file("example_input.txt") == 70


def test_solution_real_input_part_one():
    solution = Solution()
    assert solution.get_priorities_from_file("input.txt") == 8493


def test_solution_real_input_part_two():
    solution = Solution()
    assert solution.get_group_badge_from_file("input.txt") == 2552
