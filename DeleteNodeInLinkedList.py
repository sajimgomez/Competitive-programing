class ListNode :

    def __init__(self, x) :
    
        self.val = x
    
        self.next = None


class Solution :

    # 4-->(5)-->1-->9-->None
    # 4-->1-->9-->None

    # 4-->1-->9
    def deleteNode(self, node) :

        node.val = node.next.val

        node.next = node.next.next


n1 = ListNode(4)

n2 = ListNode(5)

n3 = ListNode(1)

n4 = ListNode(9)


n1.next = n2

n2.next = n3

n3.next = n4


sol = Solution()

s = sol.deleteNode(n2)

Pointer = n1

while Pointer != None :

    print(Pointer.val)

    Pointer = Pointer.next


