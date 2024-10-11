#!/usr/bin/python3
"""
Lockboxes
"""
from collections import deque


def canUnlockAll(boxes):
    """A method that determines if all the boxes can be opened."""
    if not len(boxes):
        return True

    queue = deque()
    visited = [False] * len(boxes)
    queue.append(boxes[0])
    visited[0] = True

    while len(queue):
        curr = queue.popleft()

        for v in curr:
            if 0 < v < len(boxes) and not visited[v]:
                queue.append(boxes[v])
                visited[v] = True

    return all(visited)
