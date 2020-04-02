class Solution :

    def countAndSay(self, n) :

        NumericString = '1'

        def CountAndSay2(string) :

            string += ' '

            NewString = ''

            CurrentElement = string[0]

            Counter = 1

            for i in range(1, len(string)) :

                if string[i] == CurrentElement :

                    Counter += 1

                else :

                    NewString += str(Counter) + CurrentElement

                    Counter = 1

                    CurrentElement = string[i]
                    
            
            return NewString


        for i in range(n - 1) :

            NumericString = CountAndSay2(NumericString)


        return NumericString



s = Solution()

s1 = s.countAndSay(5)

print(s1)