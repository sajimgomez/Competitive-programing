class ListNode :

    def __init__(self, val = 0, next = None) :

        self.val = val

        self.next = next


class Solution :

    def getDecimalValue(self, head) :

        Pointer = head

        MaxExp = -1

        while Pointer != None :

            Pointer = Pointer.next

            MaxExp += 1


        Sum = 0

        Pointer = head

        for i in reversed(range(MaxExp + 1)) :

            Sum += Pointer.val * 2 ** i

            Pointer = Pointer.next

        
        return Sum


n1 = ListNode(1)

n2 = ListNode(0)

n3 = ListNode(1)

n1.next = n2

n2.next = n3


sol = Solution()

s = sol.getDecimalValue(n1)

print(s)





