import sys
from collections import deque, defaultdict

def main():
    input_data = sys.stdin.buffer.read().decode()
    data = input_data.split()
    idx = 0
    N = int(data[idx]); idx += 1
    E = int(data[idx]); idx += 1
    S = int(data[idx]); idx += 1
    T = int(data[idx]); idx += 1

    edges = []
    for _ in range(E):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        edges.append((u, v))

    INF = float('inf')
    num_nodes = 2 * N

    graph = defaultdict(list)
    cap = []
    to = []

    def add_edge(u, v, c):
        graph[u].append(len(to))
        to.append(v)
        cap.append(c)
        graph[v].append(len(to))
        to.append(u)
        cap.append(0)

    for v in range(N):
        v_in = 2 * v
        v_out = 2 * v + 1
        if v == S or v == T:
            add_edge(v_in, v_out, INF)
        else:
            add_edge(v_in, v_out, 1)

    for (u, v) in edges:
        u_out = 2 * u + 1
        v_in = 2 * v
        add_edge(u_out, v_in, INF)

    source = 2 * S + 1
    sink = 2 * T

    def bfs_level():
        level = [-1] * num_nodes
        level[source] = 0
        q = deque([source])
        while q:
            u = q.popleft()
            for eid in graph[u]:
                v = to[eid]
                if cap[eid] > 0 and level[v] == -1:
                    level[v] = level[u] + 1
                    q.append(v)
        return level

    def dfs_flow(u, pushed, level, it):
        if u == sink or pushed == 0:
            return pushed
        while it[u] < len(graph[u]):
            eid = graph[u][it[u]]
            v = to[eid]
            if cap[eid] > 0 and level[v] == level[u] + 1:
                d = dfs_flow(v, min(pushed, cap[eid]), level, it)
                if d > 0:
                    cap[eid] -= d
                    cap[eid ^ 1] += d
                    return d
            it[u] += 1
        return 0

    max_flow = 0
    while True:
        level = bfs_level()
        if level[sink] == -1:
            break
        it = [0] * num_nodes
        while True:
            pushed = dfs_flow(source, INF, level, it)
            if pushed == 0:
                break
            max_flow += pushed

    print(max_flow)

if __name__ == "__main__":
    main()