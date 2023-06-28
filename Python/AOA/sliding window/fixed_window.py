arr = [1, 2, 4, 4, 3, 3]
k = 3


# O(n^2)
def dupli():
    for l in range(len(arr)):
        for r in range(l + 1, min(l + k, len(arr))):
            if arr[l] == arr[r]:
                return True, l, r
    return False


print(dupli())


def duplicate_window():
    window = set()
    l = 0
    for r in range(len(arr)):
        if r - l + 1 > k:
            window.remove(arr[l])
            l += 1
        if arr[r] in window:
            return True, l, r
        window.add(arr[r])


print(duplicate_window())
