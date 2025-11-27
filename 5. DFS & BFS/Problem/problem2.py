# 미로 탈출

'''
N X M 크기의 직사각형 형태의 미로가 있다.
미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다.
현재 위치는 (1, 1)이며 미로의 출구는 (N, M)의 위치에 존재하며 한 칸씩 이동할 때마다 1칸씩 이동한다.

괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시된다.

미로가 주어졌을 때, 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오.
(칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산)
'''


from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
print()

# 이동할 방향
# [0]번째 -> 상
# [1]번째 -> 하
# [2]번째 -> 좌
# [3]번째 ->     
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque() # 큐 생성
    queue.append((x, y)) # 시작 노드 삽입
    
    while queue:
        x, y = queue.popleft() # 큐에서 노드 추출
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위를 벗어나면, continue
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 괴물이 있으면, continue
            if graph[nx][ny] == 0:
                continue
                
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

                
    return graph[n-1][m-1]

print(bfs(0, 0))



