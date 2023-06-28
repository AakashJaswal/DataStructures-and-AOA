arr = [4, 2, 2, 4, 4, 4, 4, 3, 3, 3]

L = 0
_max = 0
for R in range(len(arr)):
    if arr[L] == arr[R]:
        _max = max(_max, R - L + 1)
    else:
        L = R
print(_max)

arr2 = [2, 3, 1, 2, 4, 3]
target = 6

L = 0
min_le = len(arr2)
_sum = 0
for R in range(len(arr2)):
    _sum += arr2[R]
    while _sum >= target:
        min_le = min(min_le, R - L + 1)
        _sum -= arr2[L]
        L += 1

print(min_le)
