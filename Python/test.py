def getConcatenation(nums: list[int]) -> list[int]:
    ans = list()
    for _ in range(2):
        for i in range(len(nums)):
            ans.append(nums[i])
    return ans


nums = [1,2,1]

print(getConcatenation(nums))


l1= [3]
l2 = [2]
val = min(l1 if l1 else l2,l2 if l2 else l1)
print(val)