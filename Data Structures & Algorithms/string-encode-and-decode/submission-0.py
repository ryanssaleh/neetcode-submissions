class Solution:

    def encode(self, strs: List[str]) -> str:
        string_so_far = ''
        for string in strs:
            string_so_far += string + '€'
        return string_so_far

    def decode(self, s: str) -> List[str]:
        split = s.split('€')
        split.pop(-1)
        return split
        