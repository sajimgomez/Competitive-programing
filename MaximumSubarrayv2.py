""" This solution uses the concept of the Kadan's algorithm, it consists 
in find the contiguous subarray who has the maximum sum of 
the contiguous subarrays from each position of the original 
array to the beginning of it, then compare the resulting 
arrays and choose the one with the biggest sum """ 

class Solution :

    def maxSubArray(self, nums) :

        MaxCurrSum = MaxSum = nums[0]

        for i in range(1, len(nums)) :

            MaxCurrSum = max(MaxCurrSum + nums[i], nums[i])

            MaxSum = max(MaxCurrSum, MaxSum)

        
        return MaxSum


s = Solution()

s1 = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])

print(s1)