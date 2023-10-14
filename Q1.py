class Solution(object):
    target=9
    def twoSum(self, nums, target):
        new=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]