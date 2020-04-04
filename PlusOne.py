class Solution :

    def plusOne(self, digits) :

        sum = 1

        for i in range(len(digits)) :

            sum += digits[i] * 10 ** (len(digits) - (i + 1))

        return [int(x) for x in str(sum)]


s = Solution()

s1 = s.plusOne([1, 2, 3])

print(s1)
        