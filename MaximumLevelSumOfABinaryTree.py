class TreeNode :

    def __init__(self, val = 0, left = None, right = None) :

        self.val = val

        self.left = left

        self.right = right


class Solution :

    def maxLevelSum(self, root) :

        max_sum = root.val

        max_sum_level = 1

        current_level = 1

        current_sum = 0

        level = [root]

        while len(level) != 0 :

            level = self.obtain_level(level)

            current_level += 1

            current_sum = self.obtain_sum_of_level(level)

            if current_sum > max_sum :

                max_sum = current_sum

                max_sum_level = current_level


        return max_sum_level

    
    def obtain_children(self, node) :

        children = []

        if node.left != None :

            children += [node.left]

        if node.right != None :

            children += [node.right]


        return children


    def obtain_level(self, children_in_level) :

        level = []

        for node in children_in_level :

            level += self.obtain_children(node)


        return level


    def obtain_sum_of_level(self, level) :

        sum_of_level = 0

        for node in level :

            sum_of_level += node.val

        
        return sum_of_level


s = Solution()

A = TreeNode(7)

B = TreeNode(1)

C = TreeNode(2)

D = TreeNode(3)

E = TreeNode(5)

F = TreeNode(6)

A.left = B

A.right = C

B.left = D

C.left = E

C.right = F

print(s.maxLevelSum(A))