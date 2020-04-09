class TreeNode :

    def __init__(self, x) :

        self.val = x

        self.left = None

        self.right = None


class Solution :

    def isSameTree(self, p, q) :

        if p == None and q == None :

            return True

        elif p == None or q == None :

            return False

        elif p.val != q.val :

            return False

        else :

            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        



pT = TreeNode(1)

pT.left = TreeNode(2)

pT.right = TreeNode(3)

qT = TreeNode(1)

qT.left = TreeNode(2)

qT.right = TreeNode(3)

s = Solution()

s1 = s.isSameTree(pT, qT)

print(s1)