from typing import List


# 左孩子
def left(i: int) -> int:
    return (i + 1) * 2 - 1


# 右孩子
def right(i: int) -> int:
    return (i + 1) * 2


def swap(a: List[int], i: int, j: int):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


# 对给定下标为i的节点，判断其与子节点的大小并进行交换
def max_heapify(a: List[int], i: int, heap_size: int):
    l = left(i)
    r = right(i)
    largest = i
    # 选取i节点、左孩子、右孩子中最大的一个作为后续交换对象
    if l < heap_size and a[l] > a[largest]:
        largest = l
    if r < heap_size and a[r] > a[largest]:
        largest = r
    if largest != i:
        swap(a, i, largest)
        # 递归修正左子树或右子树
        max_heapify(a, largest, heap_size)


def build_max_heap(vals: List[int]):
    l = len(vals)
    # 从第一个有子节点的、非叶子结点的点开始判断
    for i in range(int(l / 2), -1, -1):
        max_heapify(vals, i, l)


def get_max_heap() -> List[int]:
    val = [8, 7, 5, 1, 2, 9, 6, 3, 4]
    build_max_heap(val)
    return val

