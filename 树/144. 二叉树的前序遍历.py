"""
https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
"""
from typing import List

from 树.二叉树 import TreeNode
from 树.二叉树 import get_a_tree


# 非递归算法
def preorderTraversal(root: TreeNode) -> List[int]:
    s = []
    res = []
    p = root
    s.append(p)
    while len(s) != 0:
        p = s.pop()
        if p.right is not None:
            s.append(p.right)
        if p.left is not None:
            s.append(p.left)
        res.append(p.val)
    return res


print(preorderTraversal(get_a_tree()))