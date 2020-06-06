class ListNode :

    def __init__(self, val = 0, next = None) :

        self.val = val

        self.next = next


class Solution :

    def middleNode(self, head) :

        Pointer = head

        LinkedListSize = 0

        while Pointer != None :

            Pointer = Pointer.next

            LinkedListSize += 1

        
        if LinkedListSize % 2 == 0 :

            Position = int(LinkedListSize / 2 + 1)

            Pointer = head

            for i in range(Position - 1) :

                Pointer = Pointer.next


        else :

            Position = int((LinkedListSize + 1) / 2)

            Pointer = head

            for i in range(Position - 1) :

                Pointer = Pointer.next


        return Pointer



n1 = ListNode(1)

n2 = ListNode(2)

n3 = ListNode(3)

n4 = ListNode(4)

n5 = ListNode(5)

#n6 = ListNode(6)

n1.next = n2

n2.next = n3

n3.next = n4

n4.next = n5

#n5.next = n6


sol = Solution()

s = sol.middleNode(n1)

print(s.val)