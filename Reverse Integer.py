class Solution :

    def reverse(self, x) :

        if x < 0 :

            x = -x

            x = str(x)

            while x[len(x) - 1] == '0' :

                x = x[:len(x) - 1]


            inv_x = '-' + x[::-1]

            inv_x = int(inv_x)

        
        elif x > 0 :

            x = str(x)


            while x[len(x) - 1] == '0' :

                x = x[:len(x) - 1]


            inv_x = x[::-1]

            inv_x = int(inv_x)



        else :

        
            inv_x = x


        if inv_x < - 2 ** 31 or inv_x > 2 ** 31 - 1 :

            inv_x = 0



        return inv_x


                
numero = Solution()

ni = numero.reverse(-10230100)

print(ni)




