def bellman_ford(vertices, edges, source):
    distance = [float('inf')] * vertices
    distance[source] = 0
    steps = []

    for i in range(vertices - 1):
        step_snapshot = distance[:]
        for u, v, w in edges:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
        steps.append((i + 1, distance[:]))

    for u, v, w in edges:
        if distance[u] + w < distance[v]:
            return steps, True, distance

    return steps, False, distance
