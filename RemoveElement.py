class Solution :

    def removeElement(self, nums, val) :
        
        while val in nums :

            nums.remove(val)

        return len(nums)


s = Solution()

s1 = s.removeElement([1,2,2,3],2)

print(s1)