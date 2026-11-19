class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        if n <= 3:
            return 0

        ans = float('inf')

        for i in range(3):
            high = nums[n - 1 - i] - nums[2 - i]
            low = 0
            ans = min(ans, high + low)

        return ans
        