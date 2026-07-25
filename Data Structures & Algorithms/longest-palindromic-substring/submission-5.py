class Solution:
    def longestPalindrome(self, s: str) -> str:
        # check odd max
        if len(s) <2:
            return s
        maxl = [0,0]
        
        for i in range(len(s)):
            left = i-1
            right = i+1
            if left != -1 and right != len(s):
                if s[left] == s[right]:
                    while left != -1 and right != len(s):
                        if s[left] == s[right]:
                            left -=1
                            right +=1
                        else: 
                            break
                    left +=1
                    right -=1
                    if maxl[1]-maxl[0] < right-left:
                        maxl = [left,right]
        for i in range(len(s)-1):
            left = i
            right = i+1
            if s[left] == s[right]:
                while left != -1 and right != len(s):
                    if s[left] == s[right]:
                        left -=1
                        right +=1
                    else: 
                        break
                left +=1
                right -=1
                if maxl[1]-maxl[0] < right-left:
                    maxl = [left,right]



        
        return s[maxl[0]:maxl[1]+1]
        # check even max