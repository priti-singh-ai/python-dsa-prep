"""
Problem: Top K frequents
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.
Example:
Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]

Difficulty: Medium
Pattern: HashMap, Array,Sorting

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #count
        freq = [[] for i in range(len(nums)+1)] #frequency array

        for num in nums:
            count[num] = 1+ count.get(num,0) #calculate count of each number
        for num, cnt in count.items():
            freq[cnt].append(num) #calculate frequency of each number

        res = []
        for i in range(len(freq)-1,0,-1): #from the last value of frequency index
            for num in freq[i]: #iterate to each freq value
                res.append(num) #append it to result
                if len(res) == k: #once result and k len is equal
                    return res

