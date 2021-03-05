"""
https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
"""
from typing import List

from 树.二叉树 import TreeNode
from 树.二叉树 import get_a_tree


def levelOrder(root: TreeNode) -> List[List[int]]:
    res = []
    if root is None:
        return res

    q = [root]
    while len(q) != 0:
        result = []
        for _ in range(len(q)):
            temp = q.pop(0)
            result.append(temp.val)
            if temp.left is not None:
                q.append(temp.left)
            if temp.right is not None:
                q.append(temp.right)
        res.append(result)
    return res


print(levelOrder(get_a_tree()))