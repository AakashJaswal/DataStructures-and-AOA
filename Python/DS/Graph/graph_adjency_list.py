import collections


class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []


adj_list = {}

edges = [['A', 'B'], ['B', 'C'], ['B', 'E'], ['C', 'E'], ['E', 'D']]

for src, dst in edges:
    if src not in adj_list:
        adj_list[src] = []
    if dst not in adj_list:
        adj_list[dst] = []
    adj_list[src].append(dst)

print(adj_list)


def dfs(node, target, _list, visited):
    if node in visited:
        return 0
    if node == target:
        return 1
    count = 0
    visited.add(node)
    for ne in adj_list[node]:
        count += dfs(ne, target, _list, visited)
    visited.remove(node)
    return count


print(dfs('A', 'E', adj_list, set()))


def bfs(node, target, _list):
    q = collections.deque()
    v = set()
    q.append((node, 0))
    v.add(node)

    while q:
        for i in range(len(q)):
            n, _l = q.popleft()
            if n == target:
                return _l
            for n in _list[n]:
                if n not in v:
                    q.append((n, _l + 1))
                    v.add(n)


print(bfs('A', 'E', adj_list))
