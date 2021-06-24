"""
https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/
后序遍历[左子树 右子树 根节点]
其中，左子树所有值<根节点，右子树所有值>根节点。利用这一点判断
"""

def verifyPostorder(postorder: [int]) -> bool:
    def helper(left: int, right: int) -> bool:
        if left >= right:
            return True
        i = left
        while postorder[i] < postorder[right]:
            i += 1
        j = i
        while postorder[i] > postorder[right]:
            i += 1
        # i == right ——满足后序遍历的条件
        # helper(left, j - 1) ——对左子树递归判断
        # helper(j, right - 1) ——对右子树递归判断
        return i == right and helper(left, j - 1) and helper(j, right - 1)
    return helper(0, len(postorder) - 1)
