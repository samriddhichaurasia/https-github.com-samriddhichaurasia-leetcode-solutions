class Solution:
    def groupAnagrams(self, strs):
        d = {}
        for s in strs:
            key = tuple(sorted(s))
            d.setdefault(key, []).append(s)
        return list(d.values())