# leetcode  2520
class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        n = num   # original number save kar liya
        
        while n > 0:
            digit = n % 10   # last digit
            
            if num % digit == 0:
                count += 1
            
            n = n // 10   # last digit hata diya
        
        return count
        
