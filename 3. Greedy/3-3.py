## 숫자 카드 게임

# <규칙>
# 1. N x M 크기의 행렬로 표현되는 숫자 카드들이 있다.
# 2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
# 3. 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
# 4. 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여
#    최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.


# 1. min() 함수를 이용하는 예시

n, m = map(int, input().split()) # n: 행의 개수, m: 열의 개수

result = 0
for i in range(n):
    row = list(map(int, input().split()))
    min_value = min(row) # 현재 행에서 가장 작은 수 찾기
    result = max(result, min_value)

print(result)


# 2. 2중 반복문 구조를 이용하는 예시

'''n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    
    min_value = 10001
    # 각 숫자는 1 이상 10,000 이하이므로, 초기값을 10,001로 설정
    
    for a in data:
        min_value = min(min_value, a)
    
    retuls = max(result, min_value)

print(result)'''