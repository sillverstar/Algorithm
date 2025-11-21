## 큰 수의 법칙

n, m, k = map(int, input().split())
# N: 배열의 크기, M: 숫자가 더해지는 횟수, K: 배열의 특정한 인덱스에 대항하는 수가 연속해서 K번을 초과하여 더해질 수 없음

data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += count * first
result += (m-count) * second

print(result)