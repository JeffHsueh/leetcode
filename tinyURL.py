import random

url={}
class Codec:

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        print ("longURL: "+ longUrl)
        global url
        url={}
        if longUrl not in url.keys():
            chrset="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
            short =  "http://tinyurl.com/{}".format("".join(random.sample(chrset,5)))
            url[longUrl] = str(short)
            return url[longUrl]
        else: 
            return url[longUrl]

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        print ("shortURL: "+ shortUrl)
        print ("URL set: " + ",".join(i for i in url.keys()))
        for key,item in url.items():
            if item == shortUrl :
                return key
