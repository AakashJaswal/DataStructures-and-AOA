a = [1, 2, 3, 4, 5, 6, 7, 8]
k = 9


def binary_search_recursion(nums: list[int], s, e):
    m = (s + e) // 2

    if e - s + 1 == 0 and nums[m] != k:
        return -1

    if nums[m] == k:
        return m
    elif k < nums[m]:
        return binary_search_recursion(nums, s, m - 1)
    else:
        return binary_search_recursion(nums, m + 1, e)


def binary_search(nums: list[int], s, e):
    while s <= e:
        mid = (s + e) // 2
        if k < nums[mid]:
            e = mid - 1
        elif k > nums[mid]:
            s = mid + 1
        elif k == nums[mid]:
            return mid
    return -1


print(binary_search(a, 0, len(a) - 1))
