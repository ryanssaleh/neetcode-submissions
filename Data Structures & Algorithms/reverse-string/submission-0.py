class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = len(s) - 1
        x = 0
        while x < i:
            s[i], s[x] = s[x], s[i]
            x += 1
            i -= 1