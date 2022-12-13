from solution import Solution


def test_solution_example_part_one():
    solution = Solution()
    solution.get_sections_from_input("example_input.txt")
    assert solution.get_overlapping_sections() == 2


def test_solution_example_part_two():
    solution = Solution()
    solution.get_sections_from_input("example_input.txt")
    assert solution.get_overlapping_sections(True) == 4


def test_solution_real_input_part_one():
    solution = Solution()
    solution.get_sections_from_input("input.txt")
    assert solution.get_overlapping_sections() == 509


def test_solution_real_input_part_two():
    solution = Solution()
    solution.get_sections_from_input("input.txt")
    assert solution.get_overlapping_sections(True) == 870
