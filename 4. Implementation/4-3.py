## 왕실의 나이트

# 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동
# 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동

# c1 (-1, 2)
# b3 (2, 1)


dx = [-1, 1, -1, 1, -2, -2, 2, 2]
dy = [2, 2, -2, -2, 1, -1, 1, -1]


input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

count = 0
for i in range(len(dx)):
    nx = row + dx[i]
    ny = column + dy[i]
    
    if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
        count += 1
print(count)




'''

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1
print(result)'''