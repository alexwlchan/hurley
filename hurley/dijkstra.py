#!/usr/bin/env python
"""
This does the heavy lifting; it uses Djiksta's algorithm to find the
shortest path between podcast hosts.

Heavily cribbed from http://rosettacode.org/wiki/Dijkstra%27s_algorithm#Python
"""

from collections import namedtuple, deque
import itertools
import json
from pprint import pprint as pp


inf = float('inf')
Edge = namedtuple('Edge', ['start', 'end'])


class Graph():
    def __init__(self, edges):
        self.edges = edges2 = [Edge(*edge) for edge in edges]
        self.vertices = set(sum(([e.start, e.end] for e in edges2), []))

    def dijkstra(self, source, dest):
        assert source in self.vertices
        dist = {vertex: inf for vertex in self.vertices}
        previous = {vertex: None for vertex in self.vertices}
        dist[source] = 0
        q = self.vertices.copy()
        neighbours = {vertex: set() for vertex in self.vertices}
        for start, end in self.edges:
            neighbours[start].add((end, 1))
        # pp(neighbours)

        while q:
            u = min(q, key=lambda vertex: dist[vertex])
            q.remove(u)
            if dist[u] == inf or u == dest:
                break
            for v, cost in neighbours[u]:
                alt = dist[u] + cost
                if alt < dist[v]:  # Relax (u,v,a)
                    dist[v] = alt
                    previous[v] = u
        # pp(previous)
        s, u = deque(), dest
        while previous[u]:
            s.appendleft(u)
            u = previous[u]
        s.appendleft(u)
        return s
