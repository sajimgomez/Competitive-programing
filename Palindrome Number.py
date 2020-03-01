class Solution :

    def isPalindrome(self, x):

        x = str(x)

        ispal = False

        if '-' in x :

            ispal = False

        elif x == x[::-1] :

            ispal = True

        return ispal


numero = Solution()

num = numero.isPalindrome(121)

print(num)
      