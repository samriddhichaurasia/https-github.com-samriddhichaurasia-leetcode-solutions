class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maximum=max(nums)
        moves=0
        for i in nums :
            moves+=maximum-i
        return moves