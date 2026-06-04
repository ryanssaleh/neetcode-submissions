class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = 0
        i = len(s) - 1
        while x < i:
            if s[x].isalnum() and s[i].isalnum():
                if s[x].lower() != s[i].lower():
                    return False
                x += 1
                i -= 1
            else:
                if not s[x].isalnum():
                    x += 1
                else:
                    i -= 1
        return True
            
