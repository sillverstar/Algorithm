## 상하좌우

# N x N 크기의 정사각형 공간
# L: 왼쪽, R: 오른쪽, U: 위, D: 아래 (각각 1칸씩 이동)


n = int(input())
x, y = 1, 1
plans = input().split()


dx = [0, 0, -1, 1] # L, R, U, D
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    # 이동 좌표(nx, ny) 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    # 공간 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        countinue
    
    # 이동 수행: (x + nx, y + ny)
    x, y = nx, ny
    
print(x, y)




'''
# 1칸씩만 이동할 수 있어서, 여러 칸을 한꺼번에 이동하는 방법은 불가능

n = int(input())
data = list(map(str, input().split()))

x, y = 1, 1

for i in data:
    if i == 'L' and y > 1:
        y -= 1
    elif i == 'R' and y < n:
        y += 1
    elif i == 'U' and x > 1:
        x -= 1
    elif i == 'D' and x < n:
        x += 1
        
print(x, y)'''