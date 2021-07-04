"""
https://leetcode-cn.com/problems/path-sum-ii/
"""
from typing import List

from 树.二叉树 import TreeNode
from 树.二叉树 import get_a_tree


def pathSum(root: TreeNode, targetSum: int) -> List[List[int]]:
    result = []
    path = []

    def dfs(root: TreeNode, targetSum: int):
        if not root:
            return
        path.append(root.val)
        targetSum -= root.val
        if not root.left and not root.right and targetSum == 0:
            result.append(path[:])
        dfs(root.left, targetSum)
        dfs(root.right, targetSum)
        path.pop()

    dfs(root, targetSum)
    return result

print(pathSum(get_a_tree(), 14))