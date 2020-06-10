class Solution :
    
    def minAddToMakeValid(self, S) :

        Stack = []

        LetBehind = 0

        for i in range(len(S)) :


            if S[i] == '(' :

                Stack += [S[i]]


            elif len(Stack) != 0 :

                if S[i] == ')' :

                    Stack.pop()

            
            else : 

                LetBehind += 1

        
        return LetBehind + len(Stack)


sol = Solution()

s = sol.minAddToMakeValid(')))()(((')

print(s)






        