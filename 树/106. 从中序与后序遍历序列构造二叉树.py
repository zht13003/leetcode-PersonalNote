"""
https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
后序遍历中，数组的最后一个元素即为根节点
中序遍历序列中，以根节点为分界线，左边为左子树，右边为右子树
又假设二叉树元素不重复，可将后序遍历和中序遍历序列的根节点对应起来
"""
from typing import List

from 树.二叉树 import *


def buildTree(inorder: List[int], postorder: List[int]) -> TreeNode:
    def helper(in_left, in_right):
        # 如果这里没有节点构造二叉树了，就结束
        if in_left > in_right:
            return None

        # 选择 post_idx 位置的元素作为当前子树根节点
        val = postorder.pop()
        root = TreeNode(val)

        # 根据 root 所在位置分成左右两棵子树
        index = idx_map[val]

        # 构造右子树
        root.right = helper(index + 1, in_right)
        # 构造左子树
        root.left = helper(in_left, index - 1)
        return root

    # 建立（元素，下标）键值对的哈希表
    idx_map = {val: idx for idx, val in enumerate(inorder)}
    return helper(0, len(inorder) - 1)