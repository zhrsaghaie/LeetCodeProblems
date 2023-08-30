class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        curr = ""
        for val in s:
            if val not in curr:
                curr += val
                ans = max(ans, len(curr))
            else:
                curr = curr[curr.index(val) + 1:] + val
        return ans