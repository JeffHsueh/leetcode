class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if (n > 4) and (n%4 !=0):
            if n %(2*3) <=5:
                return True
            else:
                return False
        elif n%4 ==0:
            return False
        else:
            return True
