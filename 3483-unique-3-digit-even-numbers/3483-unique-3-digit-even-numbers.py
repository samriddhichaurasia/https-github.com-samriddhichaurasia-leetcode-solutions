class Solution:
    def totalNumbers(self, digits):
        ans = set()

        for a in range(len(digits)):
            for b in range(len(digits)):
                for c in range(len(digits)):
                    if a != b and b != c and a != c:
                      if digits[a] != 0 and digits[c]% 2 == 0:
                         ans.add(100*digits[a] + 10*digits[b] + digits[c])

        return len(ans)