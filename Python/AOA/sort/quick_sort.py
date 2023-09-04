n = [4, 3, 2, 1]


def quick_sort(nums: list[int], s, e):
    if (e - s + 1 <= 1):
        return nums

    left, pivot = s,  e

    for i in range(s, e):
        if nums[i] < nums[pivot]:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1

    nums[pivot], nums[left] = nums[left], nums[pivot]

    quick_sort(nums, s, left - 1)
    quick_sort(nums, left + 1, pivot)

    return nums


print(quick_sort(n, 0, len(n)-1))
