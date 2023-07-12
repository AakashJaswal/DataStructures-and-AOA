import sys
from collections import defaultdict


def max_val(exchanges: defaultdict(list), src: str, dest: str):
    rate = [-1.0]
    visited = set()

    # explore recursive
    def explore(_src, _dest, base=1.0):
        if _src not in exchanges or _dest not in exchanges:
            return None
        if _src == _dest:
            rate[0] = max(rate[0], base)
            return None
        visited.add(_src)
        for neighbor, parity in exchanges[_src]:
            if neighbor not in visited:
                explore(neighbor, _dest, base * parity)

    explore(src, dest)
    return rate[0]


input_data = []
for line in sys.stdin:
    input_data.append(line.strip())

graph = defaultdict(list)
for _input in input_data[0].split(';'):
    node_a, node_b, parity = _input.split(',')
    graph[node_a].append((node_b, float(parity)))
    graph[node_b].append((node_a, 1.0 / float(parity)))

print(max_val(graph, input_data[1], input_data[2]))
