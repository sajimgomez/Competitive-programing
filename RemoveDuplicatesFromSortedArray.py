class Solution :

    def removeDuplicates(self, nums) :

        nums[:] = sorted(list(set(nums)))

        return len(nums)


s = Solution()

s1 = s.removeDuplicates([1,1,2,2])

print(s1)