"""
https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
"""
from typing import List

from 树.二叉树 import TreeNode
from 树.二叉树 import get_a_tree


# 递归算法
def inorderTraversal1(root: TreeNode) -> List[int]:
    res = []
    help(root, res)
    return res


def help(root: TreeNode, res: List[int]):
    if root is None:
        return
    help(root.left, res)
    res.add(root.val)
    help(root.right, res)


# 非递归算法
def inorderTraversal2(root: TreeNode) -> List[int]:
    s = []
    res = []
    p = root
    while p is not None or len(s) != 0:
        while p is not None:
            s.append(p)
            p = p.left
        p = s.pop()
        res.append(p.val)
        p = p.right
    return res


print(inorderTraversal2(get_a_tree()))