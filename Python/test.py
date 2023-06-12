def getConcatenation(nums: list[int]) -> list[int]:
    ans = list()
    for _ in range(2):
        for i in range(len(nums)):
            ans.append(nums[i])
    return ans


nums = [1,2,1]

print(getConcatenation(nums))
