#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# no copyright, this was optimized by AI


from collections import deque


def bfs(graph, start):
    visited = []
    seen = {start}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        visited.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)

    return visited


if __name__ == "__main__":
    tree = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": [],
        "D": [],
        "E": [],
    }
    assert bfs(tree, "A") == ["A", "B", "C", "D", "E"]
    assert bfs(tree, "B") == ["B", "D", "E"]

    graph_with_cycle = {
        1: [2, 3],
        2: [4],
        3: [2],
        4: [1],
    }
    assert bfs(graph_with_cycle, 1) == [1, 2, 3, 4]
    assert bfs(graph_with_cycle, 99) == [99]
