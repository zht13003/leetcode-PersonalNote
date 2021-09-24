"""
https://leetcode-cn.com/problems/flatten-a-multilevel-doubly-linked-list/
将链表看作树，左子树是child，右子树是next
结果即为对树进行前序遍历后，将结果连接起来
"""

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def flatten(head: 'Node') -> 'Node':
    res = []
    if not head:
        return None

    def dfs(node):
        if node is None:
            return
        res.append(node)
        dfs(node.child)
        dfs(node.next)

    dfs(head)
    for i in range(0, len(res) - 1):
        j = i + 1
        res[i].next = res[j]
        res[j].prev = res[i]
        res[i].child = None
        res[j].child = None
    return res[0]