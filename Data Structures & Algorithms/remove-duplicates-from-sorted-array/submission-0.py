class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr_indx = 0
        next_indx = 1
        while next_indx < len(nums):
            if nums[curr_indx] == nums[next_indx]:
                nums.pop(next_indx)
            else:
                curr_indx, next_indx = curr_indx + 1, next_indx + 1
        return len(nums)