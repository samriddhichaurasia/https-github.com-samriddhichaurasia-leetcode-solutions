class Solution:
    def minimumSumSubarray(self, nums, l, r):
        ans = None

        for i in range(len(nums)):
            total = 0

            for j in range(i, len(nums)):
                total += nums[j]
                size = j - i + 1

                if l <= size <= r and total > 0:
                    if ans == None or total < ans:
                        ans = total

        return ans if ans != None else -1