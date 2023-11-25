
def searchInsert(self, nums: [int], target: int) -> int:
    n=0
    while(n<len(nums)):
        if nums[n] == target or nums[n] > target:
            return n
        n += 1
    return n


nums = [1,3,6,7]
target = 5
print(searchInsert(nums,target))