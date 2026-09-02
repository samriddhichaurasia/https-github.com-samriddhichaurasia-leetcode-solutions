class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            end = 0
            
            while num:
                end += num % 10
                num //= 10
            
            num = end
        
        return num