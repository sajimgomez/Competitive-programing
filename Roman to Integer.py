class Solution :

    def romanToInt(self, s):

        roma = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}

        sum = roma[s[0]]

        for i in range(1, len(s)) :

            if roma[s[i]] <= roma[s[i - 1]] :

                sum += roma[s[i]]

            else :

                sum += roma[s[i]] - 2 * roma[s[i - 1]]


        return sum


romano = Solution()

r = romano.romanToInt('III')

print(r)
