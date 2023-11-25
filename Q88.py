class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        
        for i in nums2:
            nums1.insert(0,i)
            nums1.pop()
        nums1.sort()