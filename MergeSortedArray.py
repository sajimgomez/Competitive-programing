class Solution :

    def merge(self, nums1, m, nums2, n) :

        nums1[:] = nums1[:m] + nums2

        nums1.sort()

        return nums1


s = Solution()

s1 = s.merge([1,2,3,0,0,0], 3, [2,5,6], 3)

print(s1)