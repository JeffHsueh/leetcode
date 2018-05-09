class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
                 "..-","...-",".--","-..-","-.--","--.."]
        alphabet = list(map(chr, range(97, 123)))
        temp = dict(zip((alphabet), morse))
        result = set()
        if len(words) >100:
            return None
        else:
            for i in range(0,len(words)):
                result.add(''.join( temp.get(j) for j in words[i]))
        print (result)
        return(len(result))
