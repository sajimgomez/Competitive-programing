class TreeNode :

    def __init__(self, val = 0, left = None, right = None) :

        self.val = val

        self.left = left

        self.right = right


class Solution :

    def sumEvenGrandparent(self, root) :

        sum_of_nodes_with_even_grandparents = 0

        current_level = [root]

        while len(current_level) != 0 :

            if len(self.obtain_level_of_children(current_level)) == 0 :

                break

            if len(self.obtain_level_of_children(self.obtain_level_of_children(current_level))) == 0 :

                break

            even_nodes_in_current_level = self.filter_for_even_nodes_in_level(current_level)

            if len(even_nodes_in_current_level) != 0 :

                grandchildren_of_even_grandparents = self.obtain_level_of_grandchildren(even_nodes_in_current_level)

                for node in grandchildren_of_even_grandparents :

                    sum_of_nodes_with_even_grandparents += node.val

            current_level = self.obtain_level_of_children(current_level)


        return sum_of_nodes_with_even_grandparents


    def obtain_children(self, node) :

        children = []

        if node.left != None :

            children += [node.left]

        if node.right != None :

            children += [node.right]


        return children


    def obtain_grandchildren(self, node) :

        grandchildren = []

        children = self.obtain_children(node)

        for nodes in children :

            grandchildren += self.obtain_children(nodes)


        return grandchildren


    def obtain_level_of_children(self, parents_in_level) :

        level = []

        for node in parents_in_level :

            level += self.obtain_children(node)


        return level


    def obtain_level_of_grandchildren(self, grandparents_in_level) :

        level = []

        for node in grandparents_in_level :

            level += self.obtain_grandchildren(node)


        return level


    def filter_for_even_nodes_in_level(self, level) :

        even_nodes_in_level = []

        for node in level :

            if node.val % 2 == 0 :

                even_nodes_in_level += [node]


        return even_nodes_in_level


s = Solution()

A = TreeNode(6)

B = TreeNode(7)

C = TreeNode(8)

D = TreeNode(2)

E = TreeNode(7)

F = TreeNode(1)

G = TreeNode(3)

H = TreeNode(9)

I = TreeNode(1)

J = TreeNode(4)

K = TreeNode(5)

A.left = B

A.right = C

B.left = D

B.right = E

C.left = F

C.right = G

D.left = H

E.left = I

E.right = J

G.right = K

print(s.sumEvenGrandparent(A))