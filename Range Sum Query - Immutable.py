class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.xlist = list()
        self.nums = nums
        for i in range(len(self.nums)+1):
            x = sum(self.nums[:i])
            self.xlist.append(x)
            

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        result = 0
        self.i = i
        self.j = j
        
        if i != 0:
            result =self.xlist[j+1] - self.xlist[i]
        else:
            result =self.xlist[j+1]
        return result

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
