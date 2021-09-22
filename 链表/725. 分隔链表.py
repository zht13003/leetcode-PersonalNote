"""
https://leetcode-cn.com/problems/split-linked-list-in-parts/
"""
from typing import List

from 链表.LinkList import *


def splitListToParts(head: ListNode, k: int) -> List[ListNode]:
    n = 0
    node = head
    while node:
        node = node.next
        n += 1
    remind = n % k

    result = []
    for i in range(k):
        size = n // k
        if i < remind:
            size += 1
        if size == 0:
            result.append(None)
        else:
            first, second = head, head.next
            result.append(first)
            for j in range(size - 1):
                first = first.next
                second = second.next
            first.next = None
            head = second

    return result