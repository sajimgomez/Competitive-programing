class Solution :

    def addBinary(self, a, b) :

        return str(bin(int(a, 2) + int(b, 2)))[2:]


s = Solution()

s1 = s.addBinary('11', '1')

print(s1)