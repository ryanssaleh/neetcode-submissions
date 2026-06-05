class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                elm_r, elm_l = s[l:r], s[l+1:r+1]
                return (elm_r == elm_r[::-1] or
                elm_l == elm_l[::-1])
            l, r = l + 1, r - 1
        return True


        