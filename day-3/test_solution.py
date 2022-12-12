from solution import Solution


def test_solution_example_part_one():
    solution = Solution()
    solution.get_rucksacks_from_input("example_input.txt")
    assert solution.get_priorities() == 157


def test_solution_example_part_two():
    solution = Solution()
    solution.get_rucksacks_from_input("example_input.txt")
    assert solution.get_group_badge() == 70


def test_solution_real_input_part_one():
    solution = Solution()
    solution.get_rucksacks_from_input("input.txt")
    assert solution.get_priorities() == 8493


def test_solution_real_input_part_two():
    solution = Solution()
    solution.get_rucksacks_from_input("input.txt")
    assert solution.get_group_badge() == 2552
