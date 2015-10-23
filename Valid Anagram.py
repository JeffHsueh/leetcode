## Runtime: 48 ms

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        if not (s and t) :
            return True
        alpha = [chr(i) for i in range(ord('a'),ord('z')+1)]
        for letter in alpha:
            if letter in s:
                if not letter in t:
                    return False
                else:
                    if s.count(letter) != t.count(letter):
                        return False
            elif letter in t:
                if not letter in s:
                    return False
        return True
