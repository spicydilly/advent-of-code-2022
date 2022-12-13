from solution import Solution


def test_solution_example_part_one():
    solution = Solution()
    solution.get_groupings_from_input("example_input.txt")
    assert solution.get_top_elf() == 24000


def test_solution_example_part_two():
    solution = Solution()
    solution.get_groupings_from_input("example_input.txt")
    assert solution.get_top_three_elves() == 45000


def test_solution_real_input_part_one():
    solution = Solution()
    solution.get_groupings_from_input("input.txt")
    assert solution.get_top_elf() == 71506


def test_solution_real_input_part_two():
    solution = Solution()
    solution.get_groupings_from_input("input.txt")
    assert solution.get_top_three_elves() == 209603
