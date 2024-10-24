# 풀이가 두 가지 방법이 있음. 시뮬레이션 문제라서 방향벡터를 일차원 리스트 2개, 2차원 리스트 1개로 만들 수 있음.

# 풀이 1 - 이차원 리스트를 방향 벡터로 사용
input_data = input()
row = int(input_data[1])
# a부터 h까지 영어로 표기하기에 숫자로 바꿔주는 작업
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 움직일 수 있는 경우
# 파이썬으로는 이중 리스트로도 가능함.
steps = [(-2, -1), (-1, -2), (2, -1), (-2, 1), (2, 1), (1, -2), (1, 2), (-1, 2)]

# 가능한 경우의 수를 카운트할 변수
count = 0

# 이차원 리스트에서 일차원 리스트를 하나씩 참조하면서 확인
for step in steps:
    # 이런 방식으로 일차원 리스트를 참조
    new_row = row + step[0]
    new_column = column + step[1]

    # 범위를 벗어나지 않는지 확인 후 카운트함
    if new_row >= 1 and new_row <= 8 and new_column >= 1 and new_column <= 8:
        count += 1

# 가능한 경우 출력
print(count)

# 풀이 2 - 일차원 리스트로 방향 벡터 구현 - 다른 언어로도 구현이 되는 방식임
"""
input_data = input()
row = int(input_data[1])
# a부터 h까지 영어로 표기하기에 숫자로 바꿔주는 작업
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 이차원 리스트 대신 x, y 방향 벡터를 따로 초기화
dx = [-2, -1, 2, -2, 2, 1, 1, -1]
dy = [-1, -2, -1, 1, 1, -2, 2, 2]

count = 0

for i in range(len(dx)):
    new_row = row + dy[i]
    new_column = column + dx[i]

    if new_row >= 1 and new_row <= 8 and new_column >= 1 and new_column <= 8:
        count += 1
    

print(count)
"""