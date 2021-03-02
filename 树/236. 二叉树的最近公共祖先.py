"""
https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""
from 树.二叉树 import TreeNode


class solution:
    def __init__(self):
        self.ans = None
        self.parent = {}

    # 递归
    def dfs(self, root: TreeNode, p: TreeNode, q: TreeNode) -> bool:
        if root is None:
            return False
        # 子树中是否包含p或p节点
        lson = self.dfs(root.left, p, q)
        rson = self.dfs(root.right, p, q)
        # 左子树和右子树均包含p或q节点，即该节点为公共祖先
        # 或root节点恰好是p或q节点，且左或右子树包含q或p节点，同样是公共祖先
        if (lson and rson) or ((root.val == p.val or root.val == q.val) and (lson or rson)):
            self.ans = root
        return lson or rson or (root.val == p.val or root.val == q.val)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode):
        self.dfs(root, p, q)
        return self.ans

    # 遍历树，将每个节点的父节点记录在字典中
    def dfs2(self, root: TreeNode):
        if root.left is not None:
            self.parent[root.left.val] = root
            self.dfs2(root.left)
        if root.right is not None:
            self.parent[root.right.val] = root
            self.dfs2(root.right)

    def lowestCommonAncestor2(self, root: TreeNode, p: TreeNode, q: TreeNode):
        self.dfs2(root)
        visited = []
        # 从p开始往它的祖先移动，将路径记录在visited中
        while p is not None:
            visited.append(p.val)
            p = self.parent.get(p.val)
        # 从q开始往它的祖先移动，如果路径与visited存在重合，则重合点为公共祖先
        while q is not None:
            if q.val in visited:
                return q
            q = self.parent.get(q.val)
        return None


p7 = TreeNode(7, None, None)
p4 = TreeNode(4, None, None)
p2 = TreeNode(2, p7, p4)
p6 = TreeNode(6, None, None)
p0 = TreeNode(0, None, None)
p8 = TreeNode(8, None, None)
p5 = TreeNode(5, p6, p2)
p1 = TreeNode(1, p0, p8)
p3 = TreeNode(3, p5, p1)
s = solution()
print(s.lowestCommonAncestor2(p3, p6, p4).val)
