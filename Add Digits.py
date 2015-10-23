## Runtime: 56 ms

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        str_num = str(num)
        digi=0
        while len(str_num) > 1:
            ls= []
            for i in str_num:
              ls.append(int(i))
            digi = sum(ls)
            str_num =str(digi)
        return int(str_num)
