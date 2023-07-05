a = [1, 2, 3]
subset = []


def generate_subset(idx, inner_subset):
    if idx == len(a):
        subset.append(inner_subset.copy())
        return
    generate_subset(idx + 1, inner_subset)
    inner_subset.append(a[idx])
    generate_subset(idx + 1, inner_subset)
    inner_subset.pop()


generate_subset(0, [])
print(subset)
