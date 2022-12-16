from solution import Solution


def test_solution_example_part_one():
    solution = Solution()
    solution.process_input("example_input.txt")
    assert solution.drop_sand_until_abyss() == 24


def test_solution_example_part_two():
    solution = Solution()
    solution.process_input("example_input.txt")
    assert solution.drop_sand_until_floor() == 93


def test_solution_real_input_part_one():
    solution = Solution()
    solution.process_input("input.txt")
    assert solution.drop_sand_until_abyss() == 774


def test_solution_real_input_part_two():
    solution = Solution()
    solution.process_input("input.txt")
    assert solution.drop_sand_until_floor() == 22499
