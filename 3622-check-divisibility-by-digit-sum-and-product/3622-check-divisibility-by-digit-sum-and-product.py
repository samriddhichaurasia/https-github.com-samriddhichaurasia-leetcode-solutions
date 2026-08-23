class Solution:
    def checkDivisibility(self, n: int) -> bool:
        x = n
        digit_sum = 0
        digit_prod = 1
        while x > 0 :
            digit = x % 10
            digit_sum+= digit 
            digit_prod*= digit
            x //= 10
        if n % (digit_sum + digit_prod ) == 0 :
             return True
        else :
             return False 


                   


