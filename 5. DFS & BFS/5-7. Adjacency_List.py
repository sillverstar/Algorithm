graph = [[] for _ in range(3)]



# 노드 0: (연결된 노드, 해당 노드와의 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드 1: (연결된 노드, 해당 노드와의 거리)
graph[1].append((0, 7))

# 노드 2: (연결된 노드, 해당 노드와의 거리)
graph[2].append((0, 5))

print(graph)