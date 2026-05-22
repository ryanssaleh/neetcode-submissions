class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list_so_far = []
        for i in range(len(nums)):
            less_than = nums[:i]
            greater_than = nums[i + 1: ]
            combined = less_than + greater_than
            product_so_far = combined[0]
            for x in range(1, len(combined)):
                product_so_far *= combined[x]
            list_so_far.append(product_so_far)
        return list_so_far
