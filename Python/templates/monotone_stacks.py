num = [1, 5, 2, 3, 6, 9]
res = [0] * len(num)


def mono_stack(insert_entries):
    stack = []
    for idx, entry in enumerate(insert_entries):
        while stack and stack[-1][0] <= entry:
            stack_entry, stack_idx = stack.pop()
            res[stack_idx] = [entry, idx]  # Do something with the popped item here

        stack.append([entry, idx])


mono_stack(num)
print(res)
