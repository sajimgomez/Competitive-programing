class Solution(object):
    def defangIPaddr(self, address):
        result = ""
        for letter in address:
            if letter == '.':
                result += "[.]"
            else:
                result += letter

        return result

sol = Solution()
result = sol.defangIPaddr("1.1.1.1")
print("result: ", result)