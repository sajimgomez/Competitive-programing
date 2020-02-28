class Solution :

    def twoSum(self, nums, target) :

        for i in range(len(nums)) :

            if i + 1 > len(nums) :

                break

            for j in range(i + 1, len(nums)) :

                sum = nums[i] + nums[j]

                if sum == target :

                    inds = []

                    inds += [i] + [j]

        return inds


first = Solution()

print(first.twoSum([2, 7, 11, 15], 9))






