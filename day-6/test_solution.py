from solution import Solution


def test_solution_example_part_one():
    solution = Solution()
    assert solution.process_input("example_input.txt", 4) == 7


def test_solution_example_part_one_example_two():
    solution = Solution()
    assert solution.process_input("example_input2.txt", 4) == 5


def test_solution_example_part_one_example_three():
    solution = Solution()
    assert solution.process_input("example_input3.txt", 4) == 6


def test_solution_example_part_one_example_four():
    solution = Solution()
    assert solution.process_input("example_input4.txt", 4) == 10


def test_solution_example_part_one_example_five():
    solution = Solution()
    assert solution.process_input("example_input5.txt", 4) == 11


def test_solution_example_part_two():
    solution = Solution()
    assert solution.process_input("example_input.txt", 14) == 19


def test_solution_example_part_two_example_two():
    solution = Solution()
    assert solution.process_input("example_input2.txt", 14) == 23


def test_solution_example_part_two_example_three():
    solution = Solution()
    assert solution.process_input("example_input3.txt", 14) == 23


def test_solution_example_part_two_example_four():
    solution = Solution()
    assert solution.process_input("example_input4.txt", 14) == 29


def test_solution_example_part_two_example_five():
    solution = Solution()
    assert solution.process_input("example_input5.txt", 14) == 26


def test_solution_real_input_part_one():
    solution = Solution()
    assert solution.process_input("input.txt", 4) == 1287


def test_solution_real_input_part_two():
    solution = Solution()
    assert solution.process_input("input.txt", 14) == 3716
