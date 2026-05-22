class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_so_far = []
        for num in nums:
            if num in seen_so_far:
                return True
            seen_so_far.append(num)
        return False
        