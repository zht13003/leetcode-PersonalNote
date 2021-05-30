"""
https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
前序遍历：[根节点，[左子树]，[右子树]]
中序遍历：[[左子树]，根节点，[右子树]]
"""
from typing import List
from 树.二叉树 import *


def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:
    def helper(preorder_left: int, preorder_right: int,
               inorder_left: int, inorder_right: int):
        if preorder_left > preorder_right:
            return None
        # 定位前序遍历中根节点的位置
        preorder_root = preorder_left
        # 根据根节点的值，在中序遍历中定位根节点的位置
        inorder_root = idx_map[preorder[preorder_root]]
        # 建立根节点
        root = TreeNode(preorder[preorder_root])
        # 计算左子树节点的个数
        size_left_subtree = inorder_root - inorder_left
        # 输入左子树的前序遍历和中序遍历，递归建立左子树
        # 其前序遍历是：[(删除)根节点(删除)，[左子树]，(删除)[右子树](删除)]
        # 其中序遍历是：[[左子树]，(删除)根节点，(删除)[右子树]]
        root.left = helper(preorder_left + 1, preorder_left + size_left_subtree,
                           inorder_left, inorder_root - 1)
        # 输入右子树的前序遍历和中序遍历，递归建立右子树
        # 其前序遍历是：[(删除)根节点(删除)，(删除)[左子树](删除)，[右子树]]
        # 其中序遍历是：[(删除)[左子树](删除)，(删除)根节点(删除)，[右子树]
        root.right = helper(preorder_left + size_left_subtree + 1, preorder_right,
                            inorder_root + 1, inorder_right)
        return root

    n = len(preorder)
    idx_map = {val: idx for idx, val in enumerate(inorder)}
    return helper(0, n - 1, 0, n - 1)