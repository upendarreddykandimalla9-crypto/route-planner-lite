import argparse, pandas as pd, numpy as np, os
def main(n):
    os.makedirs("data", exist_ok=True)
    nodes = []
    edges = []
    idx = 0
    for i in range(n):
        for j in range(n):
            nodes.append({"id": f"N{idx}", "x": i, "y": j})
            idx += 1
    def nid(i,j): return i*n + j
    for i in range(n):
        for j in range(n):
            a = nid(i,j)
            if i+1<n:
                b = nid(i+1,j)
                edges.append({"u": f"N{a}", "v": f"N{b}", "w": 1.0})
            if j+1<n:
                b = nid(i,j+1)
                edges.append({"u": f"N{a}", "v": f"N{b}", "w": 1.0})
    pd.DataFrame(nodes).to_csv("data/nodes.csv", index=False)
    pd.DataFrame(edges).to_csv("data/edges.csv", index=False)
    print("Wrote data/nodes.csv and data/edges.csv")
if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=10)
    a = ap.parse_args()
    main(a.n)
