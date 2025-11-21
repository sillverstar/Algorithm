## 시각

# 정수 N이 입력되면,
# 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서
# 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램 작성


n = int(input())

if n < 3:
    count = ((n + 1) * 3600) - ((n + 1)* 2025) # 3이 포함되지 않는 경우의 수
elif n < 13:
    count = ((n + 1) * 3600) - ((n) * 2025)
elif n < 23:
    count = ((n + 1) * 3600) - ((n -1) * 2025)
else:
    count = ((n + 1) * 3600) - ((n -2) * 2025)
    
    
print(count)

## 3중 for문 답안 예시

h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
                
print(count)