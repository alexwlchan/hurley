# README

This is a quick Flask app for finding links between podcasters, a la the [Six Degrees of Kevin Bacon](https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon) game.  It's a bit of nonsense that I hope will make people smile.

For the slightly longer description, see the [about page](http://six-degrees-of-myke.net/about).

### The code

This is just a simple Flask app that turns a list of podcasts and hosts into a graph, then uses [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) to find the shortest path between two hosts (if one exists).
The code for Dijkstra is taken from [Rosetta code](http://rosettacode.org/wiki/Dijkstra%27s_algorithm), because I threw this together in a hurry.

Most of this is quite messy because I threw it together quickly. It's just a bit of fun, not a serious project.

### Contributing

If you want to expand the list of podcasts, you should edit `data.json`. Each podcast gets an entry of the form `name: [list of hosts]`; for example,

```json
"Hello Internet": [
    "Brady Haran",
    "CGP Grey"
]
```

Please keep the host names alphabetically ordered, and likewise the podcasts. (I'm aware that's not quite true at the moment; I'll fix it soon, promise!)

Currently I have all the Relay.FM and 5by5 shows, plus a few others. More are always welcome. :-)
