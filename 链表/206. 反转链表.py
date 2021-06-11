"""
https://leetcode-cn.com/problems/reverse-linked-list/
"""
from 链表.LinkList import *


def reverseList(head: ListNode) -> ListNode:
    pre = None
    while head is not None:
        temp = head.next
        head.next = pre
        pre = head
        head = temp
    return pre
