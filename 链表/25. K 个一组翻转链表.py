"""
https://leetcode-cn.com/problems/reverse-nodes-in-k-group/
"""
from 链表.LinkList import *


# 对给定的头节点和尾节点，将其翻转
def reverse(head: ListNode, tail: ListNode) -> [ListNode, ListNode]:
    prev = tail.next
    p = head
    while prev != tail:
        nex = p.next
        p.next = prev
        prev = p
        p = nex
    return tail, head


def reverseKGroup(head: ListNode, k: int) -> ListNode:
    # 创建一个节点，始终指向头节点
    hair = ListNode(-1, head)
    pre = hair
    while head is not None:
        # 将tail移至k个节点后
        tail = pre
        for i in range(k):
            tail = tail.next
            if not tail:
                return hair.next
        # 记录nex为下一段节点的头节点
        nex = tail.next
        # 将该段节点翻转
        head, tail = reverse(head, tail)
        # 将上一段的尾节点与这一段的头节点相连
        pre.next = head
        # 将下一段的头节点与这一段的尾节点相连
        tail.next = nex
        # 开始下一段
        pre = tail
        head = tail.next
    return hair.next
