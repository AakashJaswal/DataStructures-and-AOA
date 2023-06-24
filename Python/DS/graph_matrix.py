# Matrix (2D Grid)
import collections

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

    path.remove((r, c))
    return count


print(dfs(grid, 0, 0, set()))


def bfs(grid):
    R, C = len(grid), len(grid[0])
    visit = set()
    q = collections.deque()

    q.append((0, 0))
    visit.add((0, 0))
    length = 0
    while q:
        for i in range(len(q)):
            r, c = q.popleft()
            if r == R - 1 and c == C - 1:
                return length

            ne = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in ne:
                if min(r + dr, c + dc) < 0 or r + dr == R or c + dc == C or (r + dr, c + dc) in visit or grid[
                    r + dr][c + dc] == 1:
                    continue
                q.append((r + dr, c + dc))
                visit.add((r + dr, c + dc))
        length += 1


print(bfs(grid))
