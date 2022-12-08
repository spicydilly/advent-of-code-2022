from solution import Solution


def test_solution_example_part_one():
    solution = Solution()
    solution.process_file("example_input.txt")
    assert solution.get_number_of_visible_trees() == 21


def test_solution_example_part_two():
    solution = Solution()
    solution.process_file("example_input.txt")
    assert solution.find_ideal_view() == 8


def test_solution_real_input_part_one():
    solution = Solution()
    solution.process_file("input.txt")
    assert solution.get_number_of_visible_trees() == 1820


def test_solution_real_input_part_two():
    solution = Solution()
    solution.process_file("input.txt")
    assert solution.find_ideal_view() == 385112
