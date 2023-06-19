n = [4, 3, 2, 1, 0]


def bucket_sort(nums: list[int]):
    val = [0] * len(set(nums))
    for i in range(len(nums)):
        val[i] += 1
    i = 0
    for j in range(len(val)):
        for k in range(val[j]):
            nums[i] = j
            i += 1

    return nums


print(bucket_sort(n))
