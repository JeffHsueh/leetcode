    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bx = format(x,"b")
        by = format(y,"b")
        if len(bx) < len(by):
            bx = bx.zfill(len(by))
        elif len(bx) > len(by):
            by = by.zfill(len(bx)) 
        return sum(e_bx!=e_by for e_bx,e_by in zip(bx,by))
