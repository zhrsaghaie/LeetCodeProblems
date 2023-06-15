class Solution:
    def rob(self, nums: List[int]) -> int:
      n = len(nums)
      ans =  [0] * (n + 2)
      for i in range(n):
          ans[i+2] = (max(ans[i+1], ans[i]+nums[i]))


      return ans[-1]