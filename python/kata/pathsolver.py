def walk():
    pass


def solve_path(start, maze, path):
    """
    Solve the path from start to end using the given path.

    :param start: Starting point of the path
    :param end: Ending point of the path
    :param path: List of points representing the path
    :return: List of points from start to end
    """
    seen = set()
    path = []
    seen.add(start)

    path.append(start)
    walk()


maze = [".########", "........#", ".#.####.#", ".#......#", ".######s#"]


solve_path(tuple(0, 0), maze, [])
