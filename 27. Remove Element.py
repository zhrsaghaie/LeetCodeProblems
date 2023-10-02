class Solution:
  def removeElement(self, nums: List[int], val: int) -> int:
    k = 0
    n = len(nums)
    for i in range(n):
      if nums[i] == val :
        k += 1
        continue
      if (i - k >= 0):
        nums[i-k] = nums[i]
    return n - k
        