from typing import Any

__all__ = (
    'Node',
    'Graph'
)


class Node(object):
    def __init__(self, value: Any):
        self.value = value

        self.outbound: list[Node] = []
        self.inbound: list[Node] = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph(object):
    def __init__(self, root: Node):
        self._root = root

    def dfs(self) -> list[Node]:
        return Graph.__dfs(self._root, [])

    @staticmethod
    def __dfs(root: Node, visited: list[Node]) -> list[Node]:
        visited.append(root)
        for node in root.outbound:
            if node not in visited:
                Graph.__dfs(node, visited)
        return visited

    def bfs(self) -> list[Node]:
        return Graph.__bfs(self._root, [self._root])

    @staticmethod
    def __bfs(root: Node, visited: list[Node]) -> list[Node]:
        unvisited = [node for node in root.outbound if node not in visited]
        visited.extend(unvisited)
        for node in unvisited:
            Graph.__bfs(node, visited)
        return visited
