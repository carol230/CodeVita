from collections import deque
import sys

def bfs_min_moves(grid, start, goal, move_rule):
    if move_rule == (0, 0):
        return -1

    m, n = len(grid), len(grid[0])
    dx, dy = move_rule
    directions = [
        (dx, dy),
        (dy, -dx),
        (-dx, -dy),
        (-dy, dx)
    ]

    queue = deque()
    queue.append((start[0], start[1], 0))
    visited = set()
    visited.add((start[0], start[1]))

    while queue:
        x, y, steps = queue.popleft()

        if (x, y) == goal:
            return steps

        for dir_x, dir_y in directions:
            nx, ny = x + dir_x, y + dir_y
            if 0 <= nx < m and 0 <= ny < n:
                if grid[nx][ny] == 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, steps + 1))

    return -1

def main():
    lines = sys.stdin.read().splitlines()
    m, n = map(int, lines[0].split())
    grid = [list(map(int, lines[i + 1].split())) for i in range(m)]
    start = tuple(map(int, lines[m + 1].split()))
    goal = tuple(map(int, lines[m + 2].split()))
    move_rule = tuple(map(int, lines[m + 3].split()))
    result = bfs_min_moves(grid, start, goal, move_rule)
    print(result, end='')

if __name__ == "__main__":
    main()
