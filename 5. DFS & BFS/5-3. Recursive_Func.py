
# 1. simple recursive function
'''
def recursive_function():
    print("This is a simple recursive function.")
    # Base case to stop recursion
    recursive_function()
    
    
recursive_function()

'''


# 2. recursive functions's finish condition
def recursive_function(i):
    if i == 100:
        return
    print(i, "번째 재귀함수에서", i + 1, "번째 재귀함수를 호출합니다.")
    recursive_function(i + 1)
    print(i, "번째 재귀함수를 종료합니다.")
    
recursive_function(1)