from collections import deque

def bfs(graph, start, visited):
    # 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
    queue = deque([start])
    visited[start] = True
    
    
    while queue:
        # 2. 큐에서 노드를 꺼내고, 
        v = queue.popleft()
        print(v, end=' ')
        
        for i in graph[v]:
            if not visited[i]:
                # 2. 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고
                queue.append(i)
                # 2. 방문 처리를 한다.
                visited[i] = True

graph = [
    [],
    [2, 4, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]


visited = [False] * 9

bfs(graph, 1, visited)