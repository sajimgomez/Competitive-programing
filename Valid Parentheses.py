class Solution :

    def isValid(self, s) :

        lista = []

        apertura = ['(', '{', '[']

        parLlavCor = {'(' : ')', '{' : '}', '[' : ']'}

        if len(s) == 0 :

            return True

        if len(s) % 2 != 0 or s[0] not in apertura or s[- 1] in apertura :

            return False 

        for i in range(len(s)) :

            if s[i] in apertura :

                lista += [s[i]]

                continue

            else :

                if parLlavCor[lista[- 1]] == s[i] :

                    lista.pop()

                else :

                    return False

        
        if len(lista) == 0 :

            return True

        
        else : 

            return False


sol = Solution()

print(sol.isValid(""))

                        
             