class Solution(object):
    def wordPattern(self, pattern, string):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pattern = str(pattern).lower()
        string = str(string).lower()
        lp=[ x for x in pattern]
        ls=[y for y in string.split(" ")]
        d= {}
        
        if len(string.split(" ")) != len(pattern):
            return False
        if len(set(lp)) != len(set(ls)):
            return False
        print ls,lp
        for key in pattern:
            d[key] =[]
            
        for i in range(len(ls)):
            d[pattern[i]].append(ls[i])
        for key ,value in d.items():
            if len(set(value)) != 1:
                return False
        return True
