n = [4, 3, 2, 1]


def ins_sort(nums: list[int] = []):
    for i in range(1, len(nums)):
        j = i - 1
        while j >= 0 and nums[j + 1] < nums[j]:
            nums[j + 1], nums[j] = nums[j], nums[j + 1]
            j -= 1
    return nums


print(ins_sort(n))
