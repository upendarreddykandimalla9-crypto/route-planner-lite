import argparse, pandas as pd, math
from heapq import heappush, heappop

def build_graph(nodes, edges):
    coords = {r["id"]:(r["x"],r["y"]) for _,r in nodes.iterrows()}
    G = {}
    for _,e in edges.iterrows():
        G.setdefault(e["u"], []).append((e["v"], float(e["w"])))
        G.setdefault(e["v"], []).append((e["u"], float(e["w"])))
    return G, coords

def h(a,b,coords):
    ax,ay = coords[a]; bx,by = coords[b]
    return abs(ax-bx)+abs(ay-by)

def astar(G, coords, start, goal):
    pq = [(0, start)]
    g = {start: 0.0}
    parent = {start: None}
    while pq:
        _, u = heappop(pq)
        if u == goal:
            break
        for v,w in G.get(u, []):
            cand = g[u]+w
            if cand < g.get(v, float("inf")):
                g[v]=cand; parent[v]=u
                f=cand+h(v,goal,coords)
                heappush(pq, (f, v))
    if goal not in parent: return [], float("inf")
    path=[]; cur=goal
    while cur is not None:
        path.append(cur); cur=parent.get(cur)
    path.reverse()
    return path, g[goal]

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", required=True)
    ap.add_argument("--goal", required=True)
    a = ap.parse_args()
    nodes = pd.read_csv("data/nodes.csv")
    edges = pd.read_csv("data/edges.csv")
    G, coords = build_graph(nodes, edges)
    path, dist = astar(G, coords, a.start, a.goal)
    print("Distance:", dist)
    print("Path:", " -> ".join(path[:20]), "...", "->" if len(path)>20 else "", path[-1] if path else "")
