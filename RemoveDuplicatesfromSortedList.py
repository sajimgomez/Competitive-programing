class ListNode :

    def __init__(self, x) :

        self.val = x

        self.next = None


class Solution :

    def deleteDuplicates(self, head) :

        if not head :

            return None

        try :

            NewList = ListNode(head.val)

            ptr = NewList

            while head :

                while head.val == ptr.val :

                    head = head.next

                ptr.next = ListNode(head.val)

                ptr = ptr.next

                head = head.next

        
        except : 

            return NewList

        
        return NewList

        


ln = ListNode(1)

ln.next = ListNode(1)

ln.next.next = ListNode(2)

ln.next.next.next = ListNode(3)

ln.next.next.next.next = ListNode(3)


s = Solution()

s1 = s.deleteDuplicates(ln)

while s1 :

    print(s1.val)

    s1 = s1.next


            


        