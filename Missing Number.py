##Runtime: 60 ms

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) ==0:
            return 0
        elif len(nums) ==1:
            if 0 not in nums:
                return 0
            elif 1 not in nums:
                return 1
        else:
            
            ls = [i for i in range(len(nums)+1)]
            
            result = sum(ls) - sum(nums)
            
        return result
