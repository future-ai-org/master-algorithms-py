#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# no copyright, this was optimized by AI


def dfs(graph, start):
    visited = []
    seen = set()

    def visit(node):
        if node in seen:
            return
        seen.add(node)
        visited.append(node)
        for neighbor in graph.get(node, []):
            visit(neighbor)

    visit(start)
    return visited


if __name__ == "__main__":
    tree = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": [],
        "D": [],
        "E": [],
    }
    assert dfs(tree, "A") == ["A", "B", "D", "E", "C"]
    assert dfs(tree, "B") == ["B", "D", "E"]

    graph_with_cycle = {
        1: [2, 3],
        2: [4],
        3: [2],
        4: [1],
    }
    assert dfs(graph_with_cycle, 1) == [1, 2, 4, 3]
    assert dfs(graph_with_cycle, 99) == [99]
