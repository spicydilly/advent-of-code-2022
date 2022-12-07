from solution import Solution


def test_solution_example_part_one():
    solution = Solution()
    solution.process_file("example_input.txt")
    assert solution.get_sum_of_directories_that_meet_size(100000) == 95437


def test_solution_example_part_two():
    solution = Solution()
    solution.process_file("example_input.txt")
    assert solution.smallest_directory_to_delete_to_meet_space(
        70000000, 30000000) == 24933642


def test_solution_real_input_part_one():
    solution = Solution()
    solution.process_file("input.txt")
    assert solution.get_sum_of_directories_that_meet_size(100000) == 1886043


def test_solution_real_input_part_two():
    solution = Solution()
    solution.process_file("input.txt")
    assert solution.smallest_directory_to_delete_to_meet_space(
        70000000, 30000000) == 3842121
