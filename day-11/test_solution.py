from solution import Solution


def test_solution_example_part_one():
    solution = Solution()
    solution.process_file("example_input.txt", 20, False)
    assert solution.get_level_monkey_business() == 10605


def test_solution_example_part_two():
    solution = Solution()
    solution.process_file("example_input.txt", 10000, True)
    assert solution.get_level_monkey_business() == 2713310158


def test_solution_real_input_part_one():
    solution = Solution()
    solution.process_file("input.txt", 20, False)
    assert solution.get_level_monkey_business() == 316888


def test_solution_real_input_part_two():
    solution = Solution()
    solution.process_file("input.txt", 10000, True)
    assert solution.get_level_monkey_business() == 35270398814
