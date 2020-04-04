class Solution :

    def maxSubArray(self, nums) :
        
        MaxSum = sum(nums)

        MaxSumArray = nums

        for i in range(1, len(nums) + 1) :

            for j in range(len(nums) - i + 1) :

                if sum(nums[j : j + i]) > MaxSum :

                    MaxSum = sum(nums[j : j + i])

                    MaxSumArray = nums[j : j + i]


        #print(MaxSumArray)

        return MaxSum


s = Solution()

s1 = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])

print(s1)
