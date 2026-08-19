class Solution():
    """
    Problem: Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
    The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
    Example:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
        
    Difficulty: Medium
    Pattern: Two Pointers, Array,Sorting
    
    Time Complexity: O(n2)
    Space Complexity: O(n2)
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i>0 and a== nums[i-1]:
                continue
            l  = i+1
            r = len(nums) -1
            while l<r:
                threesum = a + nums[l] + nums[r]
                if threesum < 0:
                    l +=1
                elif threesum > 0:
                    r -= 1
                else:
                    res.append([a,nums[l],nums[r]])
                    l +=1
                    while nums[l] == nums[l-1] and l<r:
                        l +=1
        return res