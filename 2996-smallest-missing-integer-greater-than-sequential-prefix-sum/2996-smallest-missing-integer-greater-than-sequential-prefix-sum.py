class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        sum = nums[0]
        for j in range(1,len(nums)) :
            if nums[j] == nums[j - 1] + 1 :
               sum = sum + nums[j]
            else:
                break 
        while sum in nums :
             sum = sum +1
        return sum    
    
               