import collections


class Solution:
    def numberOfSubarrays(self, nums: [int], k: int) -> int:
        answer = 0
        odd_count = 0
        prefix_count = collections.defaultdict(int)
        prefix_count[0] = 1 
        
        for num in nums:
            if num % 2 == 1:
                odd_count += 1
            
            if odd_count - k in prefix_count:
                answer += prefix_count[odd_count - k]
            
            prefix_count[odd_count] += 1
        
        return answer