"""
https://leetcode-cn.com/problems/all-paths-from-source-to-target/
"""
from typing import List


def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:
    result = []
    road = []

    def dfs(start: int):
        if start == len(graph) - 1:
            result.append(road[:])
            return
        for y in graph[start]:
            road.append(y)
            dfs(y)
            road.pop()

    road.append(0)
    dfs(0)
    return result