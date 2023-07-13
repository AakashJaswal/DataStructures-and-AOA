n, k = 5, 2

res = []


def combination_ncr(inner_res, idx):
    if len(inner_res) == k:
        res.append(inner_res.copy())
        return
    if idx > n:
        return

    for i in range(idx+1, n+1):
        inner_res.append(i)
        combination_ncr(inner_res, i)
        inner_res.pop()


combination_ncr([], 0)

# def combination(inner_res, idx):
#     if len(inner_res) == k:
#         res.append(inner_res.copy())
#         return None
#
#     if idx > n:
#         return None
#
#     inner_res.append(idx)
#     combination(inner_res, idx + 1)
#     inner_res.pop()
#     combination(inner_res, idx + 1)
#
#
# combination([], 1)
print(res)
