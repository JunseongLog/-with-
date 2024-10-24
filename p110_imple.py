# 크기 n 입력받기
n = int(input())
# 이동 경로 저장
moving_plans = input().split()

# 초기 값이 (1,1)이므로 해당 값으로 초기화
x = 1
y = 1

# 방향 벡터 설정
# L-R-U-D 순으로
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
#  move_types는 방향 벡터의 순서 그대로 만들어야 함.
move_types = ['L', 'R', 'U', 'D']

for plan in moving_plans:

    for i in range(len(move_types)):

        if (plan == move_types[i]):
            nx = x + dx[i]
            ny = y + dy[i]
        
    if (nx > n or nx < 1 or ny > n or ny < 1):
        continue
    
    x = nx
    y = ny

print(y, x)


"""
이 밑으로는 위의 코드를 이해하고 직접 코딩하기 전의 흔적.

# n입력 받기
n = int(input())
# 경로 입력받아서 리스트에 문자열로 저장
moving_plans = input().split()

# 위치 값 저장할 변수 x, y 초기화
# 시작 지점이 (1, 1)이므로 둘 다 1로 초기화
x = 1
y = 1

# 이동 계획의 값을 하나씩 참조하면서 x, y의 값을 조정
for value in moving_plans:
    if (value == 'L' and (x - 1) >= 1):
        x -= 1
    elif (value == 'R' and (x + 1) <= n):
        x += 1
    elif (value == 'U' and (y-1) >= 1):
        y -= 1
    elif (value == 'D' and (y + 1) <= n):
        y += 1

print(y, x, sep=" ")

"""

"""
# 이 밑부터는 책의 풀이임. 근데 직관적이지가 않은 것 같음. 이해가 잘 안됨.
# 굳이 이렇게 풀어야 하나 싶음.

n = int(input())
x, y = 1, 1
plans = input().split()

# L R U D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어난는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)

"""























        