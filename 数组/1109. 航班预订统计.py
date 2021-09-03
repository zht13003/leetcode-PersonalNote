"""
https://leetcode-cn.com/problems/corporate-flight-bookings/
引入差分数组d[i]=list[i]-list[i-1]
对差分数组求前缀和数组即为原数组
当对一个区间[l,r]同时加上一个数n时，d[l] += n，d[r+1] -= n
这样就把对区间的修改变为了对两个数的修改
"""
from typing import List


def corpFlightBookings(bookings: List[List[int]], n: int) -> List[int]:
    nums = [0] * n
    for left, right, inc in bookings:
        nums[left - 1] += inc
        if right < n:
            nums[right] -= inc

    for i in range(1, n):
        nums[i] += nums[i - 1]

    return nums