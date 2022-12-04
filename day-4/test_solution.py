from solution import Solution


def test_solution_example_part_one():
    solution = Solution()
    assert solution.get_overlapping_sections_from_file(
        "example_input.txt") == 2


def test_solution_example_part_two():
    solution = Solution()
    assert solution.get_overlapping_sections_from_file(
        "example_input.txt", True) == 4


def test_solution_real_input_part_one():
    solution = Solution()
    assert solution.get_overlapping_sections_from_file("input.txt") == 509


def test_solution_real_input_part_two():
    solution = Solution()
    assert solution.get_overlapping_sections_from_file(
        "input.txt", True) == 870
