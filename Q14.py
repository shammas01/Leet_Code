from aiohttp_retry import List


class Solution:
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
            
        strs.sort()

        first_str = strs[0]
        last_str = strs[-1]

        common_prefix = ""
        min_len = min(len(first_str), len(last_str))

        for i in range(min_len):
            if first_str[i] == last_str[i]:
                common_prefix += first_str[i]
            else:
                break

        return common_prefix