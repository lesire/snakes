import snakes.plugins
snakes.plugins.load("gv", "snakes.nets", "snk")
from snk import *

n = loads(",railroad.pnml")
g = StateGraph(n)
for s in g :
    m = g.net.get_marking()
    # safety property: train present => gates closed
    if ("train().crossing" in m
        and True in m["train().crossing"]
        and "closed" not in m["gate().state"]) :
        print s, m
print "checked", len(g), "states"
g.draw(",rr-states.png")
