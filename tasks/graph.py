from collections import deque
from typing import Any, Deque, List

__all__ = (
    'Node',
    'Graph'
)

class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound: List[Node] = []
        self.inbound: List[Node] = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root: Node = root

    def dfs(self) -> list[Node]:
        visited: List[Node] = []
        stack: Deque[Node] = deque()
        stack.appendleft(self._root)
        while len(stack) != 0:
            current = stack.popleft()
            if current in visited:
                continue
            for node in reversed(current.outbound):
                stack.appendleft(node)
            visited.append(current)
        return visited

    def bfs(self) -> list[Node]:
        visited: List[Node] = []
        heap: Deque[Node] = deque()
        heap.append(self._root)
        while len(heap) != 0:
            current = heap.popleft()
            if current in visited:
                continue
            for node in current.outbound:
                heap.append(node)
            visited.append(current)
        return visited
