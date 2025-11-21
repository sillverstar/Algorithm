## 1이 될 때까지


# 1. 시간 복잡도 고려

n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    # 몫 ex) 25 3 -> (25 // 3) * 3 = 8 * 3 = 24
    
    # 빼기 카운트
    n = target
    result += (n - target)
    
    if n < k:
        break
    
    # 나누기 카운트
    result += 1
    n //= k

result += (n - 1)
print(result)
    
    
    

# 2. 단순하게 푸는 답안 예시

'''n, k = map(int, input().split())
result = 0

while n >= k:
    while n % k != 0: # n을 k로 나눈 나머지가 0이 아닐 때 True == 나누어 떨어지지 않을 때
        n -= 1
        result += 1
    n //= k
    result += 1
    
# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1
    
print(result)


'''





# ------------------------------------------------------
'''
n, k = map(int, input().split())

result = 0

while True:
    target = (n//k) * k
    # 몫 ex) 25 3 -> (25 // 3) * 3 = 8 * 3 = 24
    result += (n - target) 
    # 횟수를 result에 더함 ex) result += 25 - 4 = 1
    n = target
    # k로 나누어지는 가장 큰 정수까지 1을 뺀 값을 n에 저장 ex) n = target = 24

    if n < k:
        break # n이 k보다 작을 때(더 이상 나눌 수 없을 때) break

    # k로 나누기, 횟수는 result++
    result += 1
    n //= k


# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)
'''




'''
N, K = map(int, input().split())

count = 0
while N != 1:
    if N % K == 0:
        N /= K
    else:
        N -= 1

    count += 1

print(count)

# 이 경우 계산은 가능하지만
# 위쪽 코드는 whlie문을 한 번 돌 때마다 나눗셈을 시행하기 때문에
# 숫자가 커질수록 시간복잡도의 차이가 커지게 됨
'''


'''
K가 2 이상일 경우에는 (K로 나누는 것)이 (1을 빼는 것)보다 항상 빠름

'''