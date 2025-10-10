def dijkstra_matrix_array(G, s):
    V = len(G)
    INF = float('inf')
    dist = [INF] * V
    prev = [None] * V
    visited = [False] * V
    dist[s] = 0

    for _ in range(V):
        # Extract-min: find vertex u with minimal dist[u] among unvisited
        u = None
        min_dist = INF
        for i in range(V):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i
        if u is None:
            break  # Remaining vertices are inaccessible
        visited[u] = True

        # Relax edges for vertex u
        for v in range(V):
            if not visited[v] and G[u][v] is not None and G[u][v] != INF:
                alt = dist[u] + G[u][v]
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
    return dist, prev