class Solution():
    """
    Problem: Given an array of integers numbers that is sorted in non-decreasing order.
    Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.
    There will always be exactly one valid solution.
    Example:
    Input: numbers = [1,2,3,4], target = 3

    Output: [1,2]
    
    Difficulty: Medium
    Pattern: Two Pointers, Array,Sorting
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    def sortedTwoSum(self, numbers:List[int], target:int)-> List[int]:
        l=0
        r =len(numbers)-1

        while l<r:
            currSum = numbers[l]+numbers[r]
            if currSum < target:
                l +=1
            elif currSum > target:
                r-= 1
            else:
                return[l+1,r+1]
        return []