class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        import itertools
        return list(itertools.permutations(nums))