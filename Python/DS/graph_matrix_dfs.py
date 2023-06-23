# Matrix (2D Grid)
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]


def dfs(grid, r, c, path: set):
    R = len(grid)
    C = len(grid[0])

    if min(r, c) < 0 or r == R or c == C or (r, c) in path or grid[r][c] == 1:
        return 0
    if r == R - 1 and c == C - 1:
        return 1

    path.add((r, c))

    count = 0
    count += dfs(grid, r + 1, c, path)
    count += dfs(grid, r - 1, c, path)
    count += dfs(grid, r, c + 1, path)
    count += dfs(grid, r, c - 1, path)

    path.remove((r ,c))
    return count


print(dfs(grid, 0, 0, set()))