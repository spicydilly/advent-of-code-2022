from solution import Solution


def test_solution_example_part_one():
    solution = Solution()
    solution.process_input("example_input.txt", 2)
    assert solution.number_of_locations_visited_by_last_knot() == 13


def test_solution_example_part_two():
    solution = Solution()
    solution.process_input("example_input.txt", 10)
    assert solution.number_of_locations_visited_by_last_knot() == 1


def test_solution_example_two_part_two():
    solution = Solution()
    solution.process_input("example_input2.txt", 10)
    assert solution.number_of_locations_visited_by_last_knot() == 36


def test_solution_real_input_part_one():
    solution = Solution()
    solution.process_input("input.txt", 2)
    assert solution.number_of_locations_visited_by_last_knot() == 5960


def test_solution_real_input_part_two():
    solution = Solution()
    solution.process_input("input.txt", 10)
    assert solution.number_of_locations_visited_by_last_knot() == 2327
