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
            rw, cl = q.popleft()
            if rw == R - 1 and cl == C - 1:
                return length

            ne = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for rd, cd in ne:
                r, c = rw + rd, cl + cd
                if min(r, c) < 0 or r == R or c == C or (r, c) in visit or grid[r][c] == 1:
                    continue
                q.append((r, c))
                visit.add((r, c))
        length += 1


print(bfs(grid))
