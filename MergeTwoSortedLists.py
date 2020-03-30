class ListNode :


    def __init__(self, x) :

        self.val = x

        self.next = None



class Solution :

    def mergeTwoLists(self, l1, l2) :


        if l1 == None and l2 == None :

            return None

        
        if l1 == None and l2 != None :

            return l2


        if l2 == None and l1 != None :

            return l1
        

        NewList = ListNode(None)

        pointer = NewList

        while not(l1 == None and l2 == None) :


            if l1 == None and l2 != None :

                pointer.next = l2

                return NewList.next


            if l2 == None and l1 != None :

                pointer.next = l1

                return NewList.next


            if l1.val <= l2.val :

                pointer.next = ListNode(l1.val)

                l1 = l1.next

            elif l1.val > l2.val :

                pointer.next = ListNode(l2.val)

                l2 = l2.next

            
            pointer = pointer.next


        return NewList.next





lc1 = ListNode(1)

lc1.next = ListNode(2)

lc1.next.next = ListNode(4)

lc2 = ListNode(1)

lc2.next = ListNode(3)

lc2.next.next = ListNode(4)

s = Solution()

s1 = s.mergeTwoLists(lc1, lc2)

while s1 != None :

    print(s1.val)

    s1 = s1.next










        









            