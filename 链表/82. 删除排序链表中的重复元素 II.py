"""
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/
"""
from 链表.LinkList import *


def deleteDuplicates(head: ListNode) -> ListNode:
    null = ListNode(-1, head)
    if not head:
        return head
    node = null
    while node.next and node.next.next:
        # 若两节点值相等，循环跳过节点直到不相等
        if node.next.val == node.next.next.val:
            target = node.next.val
            while node.next and node.next.val == target:
                node.next = node.next.next
        else:
            node = node.next
    return null.next