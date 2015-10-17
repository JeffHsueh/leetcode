class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d= {}
        for key in nums:
            d[key] = []
        for i in nums:
            d[i].append(i)
            
        for key ,value in d.items():
            if len(value) >= 2:
                result = d[key].pop()
                return int(result)
