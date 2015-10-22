## Runtime: 64 ms

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        result = []
        for num in nums:
            dic[num] = int(dic.get(num,0)) + 1
        
        for k,v in dic.items():
            if v == 1:
                result.append(k)
        
        return result
