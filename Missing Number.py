##Runtime: 60 ms

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) ==0:
            return 0
        
        else:
            
            ls = [i for i in range(len(nums)+1)]
            
            result = sum(ls) - sum(nums)
            
        return result
