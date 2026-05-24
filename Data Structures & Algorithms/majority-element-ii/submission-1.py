class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_freq = {}
        for num in nums:
            if num not in nums_freq:
                nums_freq[num] = 1
            else:
                nums_freq[num] += 1
       
        greater_than_so_far = []
        for num in nums_freq:
            if nums_freq[num] > len(nums) // 3:
                greater_than_so_far.append(num)
        return greater_than_so_far