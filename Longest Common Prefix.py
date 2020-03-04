class Solution :

    def longestCommonPrefix(self, strs) :

        if strs == [] :

            return ''

        menor = strs[0]

        for i in range(len(strs)) :

            if len(strs[i]) < len(menor) :

                menor = strs[i]

        cond = True

        while cond :

            for i in range(len(strs)) :

                if strs[i].startswith(menor) :

                    if i == len(strs) - 1 and strs[i].startswith(menor) :

                        cond = False

                        break

                    continue

                else :

                    menor = menor[:len(menor) - 1]

                    break

        
        return menor


#pr = Solution()

#print(pr.longestCommonPrefix(['a', 'aa'])) 

#print(pr.longestCommonPrefix(['aa', 'a'])) 

#print(pr.longestCommonPrefix(["flower","flow","flight"])) 

#print(pr.longestCommonPrefix(["dog","racecar","car"])) 

#print(pr.longestCommonPrefix(['a'])) 

#print(pr.longestCommonPrefix(['a', 'a'])) 

#print(pr.longestCommonPrefix(['aa', 'aa']))

#print(pr.longestCommonPrefix([]))

#print(pr.longestCommonPrefix(['']))