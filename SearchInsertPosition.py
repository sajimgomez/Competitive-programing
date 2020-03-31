class Solution :

    def searchInsert(self, nums, target) :

        if target not in nums :

            nums.append(target)

            nums.sort()

            return nums.index(target)

        return nums.index(target)


s = Solution()

s1 = s.searchInsert([1,3,5,6], 2)

print(s1)

