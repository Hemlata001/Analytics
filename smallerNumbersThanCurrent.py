# leetcode 1365
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # pehle hume 2 loop lene padege i j i = 0 se hoga j = i+1 se aur usme chhote ko count kregaa
        # ek list bnaa dege usme count ko likhte rahege aesa kuch hogaa
        result = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            result.append(count)
        
        return result

