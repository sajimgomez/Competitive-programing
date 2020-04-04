class Solution :

    def lengthOfLastWord(self, s) :

        return len(s.strip().rsplit(' ')[len(s.strip().rsplit(' ')) - 1])


s = Solution()

s1 = s.lengthOfLastWord('a ')

print(s1)