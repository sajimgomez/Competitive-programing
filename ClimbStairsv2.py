class Solution :

    def climbStairs(self, n) :

        if n == 1 :

            return 1

        elif n == 2 :

            return 2

        else :

            f_n_1 = 2

            f_n_2 = 1

            for i in range(3, n + 1) :

                f_n = f_n_1 + f_n_2

                f_n_2 = f_n_1

                f_n_1 = f_n


            return f_n


s = Solution()

s1 = s.climbStairs(5)

print(s1)