class Solution :

    def dailyTemperatures(self, T) :

        DaysUntilNextWarmerTemp = [0] 

        Stack = [len(T) - 1]

        for i in reversed(range(len(T) - 1)) :

            if T[i] < T[Stack[-1]] :

                DaysUntilNextWarmerTemp.insert(0, Stack[-1] - i)

                Stack += [i]

            else :

                while T[i] >= T[Stack[-1]] :

                    Stack.pop()

                    if len(Stack) == 0 :

                        DaysUntilNextWarmerTemp.insert(0, 0)

                        Stack += [i]

                        break


                    if T[i] < T[Stack[-1]] :

                        DaysUntilNextWarmerTemp.insert(0, Stack[-1] - i)

                        Stack += [i]

                        break


        return DaysUntilNextWarmerTemp                    


sol = Solution()

s = sol.dailyTemperatures([89,62,70,58,47,47,46,76,100,70])

print(s)