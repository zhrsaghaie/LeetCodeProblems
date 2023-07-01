class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        current = nums[0]
        for i in range(1, len(nums)):
            current += nums[i]
            if nums[i] > current:
                current = nums[i]
            maxSum = max(maxSum, current)

        return maxSum
