class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=""
        for i in s:
            if i.isalnum():
                res=res+i
        
        res=res.lower()
        
        revres=res[::-1]

        if(res==revres):
            return True
        return False