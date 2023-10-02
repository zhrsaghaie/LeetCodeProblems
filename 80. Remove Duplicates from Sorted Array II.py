class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    holder = nums[0]
    counter = 0
    n  = len (nums)
    k = 0
    for i in range(len(nums)):
        nums[i - k] = nums[i]
        if nums[i - k] == holder:
            counter += 1
            if counter > 2:                          
                k += 1       
        else:
            holder = nums[i - k]
            counter = 1
    return len(nums)- k