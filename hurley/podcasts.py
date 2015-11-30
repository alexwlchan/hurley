import itertools
import json

from hurley.dijkstra import Graph

import os
with open("/var/www/six-degrees-of-myke/hurley/data.json") as f:
    data = json.loads(f.read())

pairings = set()
podcasters = set()
for value in data.values():
    for person in value:
        podcasters.add(person)
    for i in itertools.permutations(value, 2):
        pairings.add(i)
pairings = list(pairings)

graph = Graph(pairings)


def find_links(result):
    pairings = []
    for i in xrange(len(result) - 1):
        pair = list(result)[i:i+2]
        for podcast, podcasters in data.iteritems():
            if all(item in podcasters for item in list(pair)):
                pairings.append((pair[0], pair[1], podcast))
    return pairings
