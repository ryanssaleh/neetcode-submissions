class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list_so_far = []

        for i in range(len(nums)):

            less_than = nums[:i]

            greater_than = nums[i + 1:]

            combined = less_than + greater_than

            product_so_far = 1

            for x in combined:

                product_so_far *= x

            list_so_far.append(product_so_far)

        return list_so_far