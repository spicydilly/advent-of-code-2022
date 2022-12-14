from solution import Solution


def test_solution_example_part_one():
    solution = Solution()
    solution.process_input("example_input.txt")
    assert solution.indices_of_pairs_in_order() == 13


def test_solution_example_part_two():
    solution = Solution()
    solution.process_input("example_input.txt")
    assert solution.decoder_key() == 140


def test_solution_real_input_part_one():
    solution = Solution()
    solution.process_input("input.txt")
    assert solution.indices_of_pairs_in_order() == 6072


def test_solution_real_input_part_two():
    solution = Solution()
    solution.process_input("input.txt")
    assert solution.decoder_key() == 22184
