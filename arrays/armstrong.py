class Solution():
    def is_armstrong(self, nums:int)-> bool:
        power = len(str(nums))

        total_sum = 0 
        temp = nums

        while temp > 0:
            digit = temp%10
            total_sum += digit**power
            temp//=10
        return total_sum == nums

    if __name__ == __main__:
        s= Solution()
        s.is_armstrong(153)