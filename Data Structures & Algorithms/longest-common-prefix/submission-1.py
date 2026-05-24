class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix_so_far = ''
        min_length = min([len(x) for x in strs])
        for i in range(min_length):
            if all(strs[0][i] == strs[x][i] for x in range(1, len(strs))):
                prefix_so_far += strs[0][i]
            else:
                return prefix_so_far
        return prefix_so_far