class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        list_so_far = []
        l = 0
        while l < len(nums):
            if l == 0 or nums[l] != nums[l - 1]:
                left, right = l + 1, len(nums) - 1
                while left < right:
                    s = nums[l] + nums[left] + nums[right]
                    if s < 0:
                        left += 1
                    elif s > 0:
                        right -= 1
                    else:
                        list_so_far.append([nums[l], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
            l += 1
        return list_so_far

            