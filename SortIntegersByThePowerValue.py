class Solution :

    def getKth(self, lo, hi, k) :

        list_of_integers_in_between = [i for i in range(lo, hi + 1)]

        list_of_integers_in_between.sort(key = self.obtain_power)

        return list_of_integers_in_between[k - 1]


    def obtain_power(self, x) :

        power = 0

        while x != 1 :

            if x % 2 == 0 :

                x /= 2

            else :
                
                x = 3 * x + 1

            power += 1

        
        return power


s = Solution()

print(s.getKth(12, 15, 2))

