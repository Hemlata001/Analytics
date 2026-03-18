# leetcode 1281
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        Sum = 0
        Product = 1
        
        while n > 0:
            digit = n % 10
            
            Sum += digit
            Product *= digit
            
            n = n // 10
        
        return Product - Sum
