"""
https://leetcode-cn.com/problems/linked-list-cycle-ii/
"""
from 链表.LinkList import *


# 将访问过的节点放入集合内
def detectCycle(head: ListNode) -> ListNode:
    pos = head
    visited = set()
    while pos is not None:
        if pos in visited:
            return pos
        else:
            visited.add(pos)
        pos = pos.next


# 慢指针每次走一个，快指针每次走两个，最终会在环中相遇。此时从头节点中再出发一个慢指针，与之前的慢指针一起前进，最终会在入环点相遇
def detectCycle2(head: ListNode) -> ListNode:
    if head is None:
        return None
    slow = head
    fast = head
    while fast is not None:
        slow = slow.next
        if fast.next is not None:
            fast = fast.next.next
        else:
            return None
        if fast == slow:
            ptr = head
            while ptr != slow:
                ptr = ptr.next
                slow = slow.next
            return ptr
    return None


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d
d.next = b
print(detectCycle2(a).val)