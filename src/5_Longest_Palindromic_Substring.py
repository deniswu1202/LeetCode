class Solution(object):
    def LongestPalindrome(self, s):
        sLen=len(s)
        pStart, pEnd = 0, 0
        pSet=set()
        for i in xrange(0,sLen): 
            pSet.add((i,i))
            pSet.add((i,i-1))

        for k in xrange(2,sLen+1):
            for i in xrange(0,sLen):
                if i+k-1 < sLen and s[i] == s[i+k-1] and (i+1,i+k-2) in pSet:
                    pStart, pEnd = i, i+k-1
                    pSet.add((i,i+k-1))
        return s[pStart:pEnd+1]

a = Solution()   
print a.LongestPalindrome('dddd')
