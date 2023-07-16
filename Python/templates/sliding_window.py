def maxSubArrayLen(nums: list[int], target: int) -> int:
    _sum = 0  # Window
    max_len = 0  # Answer
    L = 0

    for R in range(len(nums)):
        _sum += nums[R]  # Append to window

        while _sum > target and L <= R:  # Window is invalid here
            _sum -= nums[L]  # Remove left until window is valid
            L += 1

        max_len = max(max_len, R - L + 1)  # Could be the answer

    return max_len


def minSubArrayLen(nums: list[int], target: int) -> int:
    _sum = 0  # Window
    min_len = len(nums) + 1  # Answer
    L = 0

    for R in range(len(nums)):
        _sum += nums[R]  # Append to window

        while _sum >= target:  # Window is valid here
            min_len = min(min_len, R - L + 1)  # Could be the answer
            _sum -= nums[L]  # Remove left until allowed for minimum
            L += 1

    return 0 if min_len == len(nums) + 1 else min_len


target = 7
nums = [2, 3, 1, 1, 2, 4, 3]

# Largest window where sum <= target
print(maxSubArrayLen(nums, target))

# Minimum window where sum >= target
print(minSubArrayLen(nums, target))
