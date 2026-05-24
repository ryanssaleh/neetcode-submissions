class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_freq = {}
        for num in nums:
            if num not in nums_freq:
                nums_freq[num] = 1
            else:
                nums_freq[num] += 1
        nums_freq_sorted = sorted(list(nums_freq.items()), key=lambda tup: tup[1], reverse=True)      
        nums_so_far = []
        for i in range(k):
            nums_so_far.append(nums_freq_sorted[i][0])
        return nums_so_far