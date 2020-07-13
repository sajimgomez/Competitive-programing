class TreeNode :

    def __init__(self, val = 0, left = None, right = None) :

        self.val = val

        self.left = left

        self.right = right


class Solution :

    def deepestLeavesSum(self, root) :

        sum_of_deepest_leaves = 0

        current_level = [root]

        while True :

            if len(self.obtain_level_from_previous_one(current_level)) ==  0 :

                for node in current_level :

                    sum_of_deepest_leaves += node.val

                break

            current_level = self.obtain_level_from_previous_one(current_level)


        return sum_of_deepest_leaves 


    def obtain_children(self, node) :

        children = []

        if node.left != None :

            children += [node.left]

        if node.right != None :

            children += [node.right]


        return children


    def obtain_level_from_previous_one(self, previous_level) :

        level = []

        for node in previous_level :

            level += self.obtain_children(node)


        return level


s = Solution()

A = TreeNode(1)

B = TreeNode(2)

C = TreeNode(3)

D = TreeNode(4)

E = TreeNode(5)

F = TreeNode(6)

G = TreeNode(7)

H = TreeNode(8)

A.left = B

A.right = C

B.left = D

B.right = E

C.right = F

D.left = G

F.right = H

print(s.deepestLeavesSum(A))