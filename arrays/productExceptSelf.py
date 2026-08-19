class Solution():
    """
    Problem: Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?
Example:
Input: nums = [1,2,4,6]

Output: [48,24,12,8]

Difficulty: Medium
Pattern: HashMap, Array,Sorting

Time Complexity: O(n)
Space Complexity: O(n)
    """
    def productExceptSelf(self, nums:List[int]) -> List[int]:
        res = [0]*(len(nums))
        prefix = 1
        postfix=1

        for i in range(len(nums)):
            res[i] =prefix
            prefix = prefix*nums[i]
        for j in range(len(nums)-1,-1,-1):
            res[j] =res[j]*postfix
            postfix = postfix*nums[j]
        return res