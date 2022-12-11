from solution import Solution


def test_solution_example_part_one():
    solution = Solution()
    solution.process_file("example_input.txt")
    assert solution.sum_signal_monitor() == 13140


def test_solution_example_part_two():
    solution = Solution()
    solution.process_file("example_input.txt")
    assert solution.get_crt() == """
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######....."""


def test_solution_real_input_part_one():
    solution = Solution()
    solution.process_file("input.txt", )
    assert solution.sum_signal_monitor() == 12520


def test_solution_real_input_part_two():
    solution = Solution()
    solution.process_file("input.txt")
    assert solution.get_crt() == """
####.#..#.###..####.###....##..##..#....
#....#..#.#..#....#.#..#....#.#..#.#....
###..####.#..#...#..#..#....#.#....#....
#....#..#.###...#...###.....#.#.##.#....
#....#..#.#....#....#....#..#.#..#.#....
####.#..#.#....####.#.....##...###.####."""
