from solution import Solution


def test_solution_example_part_one():
    solution = Solution()
    solution.process_input("example_input.txt")
    assert solution.traverse_start_to_end() == 31


def test_solution_example_part_two():
    solution = Solution()
    solution.process_input("example_input.txt")
    assert solution.traverse_each_a_to_end() == 29


def test_solution_real_input_part_one():
    solution = Solution()
    solution.process_input("input.txt")
    assert solution.traverse_start_to_end() == 449


def test_solution_real_input_part_two():
    solution = Solution()
    solution.process_input("input.txt")
    assert solution.traverse_each_a_to_end() == 443
