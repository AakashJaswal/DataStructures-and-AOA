n = [4, 3, 2, 1]


def merge_sort(nums: list[int], start, end):
    if (end == start):
        return nums
    middle = (start + end) // 2
    merge_sort(nums, start, middle)
    merge_sort(nums, middle + 1, end)

    merge(nums, start, middle, end)
    return nums


def merge(nums, start, middle, end):
    L = nums[start: middle + 1]
    R = nums[middle + 1: end + 1]

    i, j, k = 0, 0, start

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            nums[k] = L[i]
            i += 1
        else:
            nums[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        nums[k] = L[i]
        k, i = k+1, i+1
    while j < len(R):
        nums[k] = R[j]
        k, j = k+1, j+1


print(merge_sort(n, 0, len(n)))
