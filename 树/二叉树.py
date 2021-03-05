class TreeNode:
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right


'''
         3
        / \
       5    1
      / \  / \
     6  2  0  8
       / \
      7   4
'''
def get_a_tree():
    p7 = TreeNode(7, None, None)
    p4 = TreeNode(4, None, None)
    p2 = TreeNode(2, p7, p4)
    p6 = TreeNode(6, None, None)
    p0 = TreeNode(0, None, None)
    p8 = TreeNode(8, None, None)
    p5 = TreeNode(5, p6, p2)
    p1 = TreeNode(1, p0, p8)
    p3 = TreeNode(3, p5, p1)
    return p3
