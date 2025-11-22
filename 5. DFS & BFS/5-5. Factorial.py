# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 재귀적으로 구현한 n!
def factorial_recursive(n):
    # n! = n * (n-1)!
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

print("반복 구현: ", factorial_iterative(5))
print("재귀 구현: ", factorial_recursive(5))


'''
팩토리얼은 n이 양의 정수일 때만 유효
-> n이 1 이하인 경우 1을 반환하도록 설정해야함
'''