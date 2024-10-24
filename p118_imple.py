# p118 게임 개발 (시뮬레이션)

# 맵의 크기 입력 받기
n, m = map(int, input().split())
# 시작 좌표와 바라보는 방향 입력 받기
x, y, direction = map(int, input().split())

# 리스트를 두 가지 사용함. check_list(모두 0으로 초기화 해놓고 지나간 곳은 1로 바꿔줄 거임)와 map(사용자에게 받는 육지, 바다 총 지형.)
# 근데 하나만 쓰면 안되나? - 지형은 불변인 상태인 원본으로 두는 것이 좋기 때문에 check_list를 사용하는 거임.

# 리스트 컴프리헨션으로 리스트 생성 및 0으로 초기화
check_list = [[0]* m for i in range(n)]
# 출발 좌표 방문 처리
check_list[x][y] = 1

# 지도 데이터 받기
game_map = []
for i in range(n):
    game_map.append(list(map(int, input().split())))

# 방향 벡터 북-동-남-서 순 (입력조건이 0부터 3까지 북-동-남-서 순이기 때문)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1

    if direction == -1:
        direction = 3


# 처음 시작 좌표 표함이므로 1로 시작
count = 1
# 왼쪽으로 4번 다 돌았을 때는 뒤로 가줘야 하기에 변수 하나에 돌아간 횟수 저장
turn_times = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 육지이면서 가보지 않은 곳 일때
    if (game_map[nx][ny] == 0 and check_list[nx][ny] == 0):
        x = nx
        y = ny
        check_list[x][y] = 1
        count += 1
        # 움직이고 난 이후이니 turn_times 0 대입
        turn_times = 0
    else:
        turn_times += 1
    
    if turn_times == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if game_map[nx][ny] == 0:
            x = nx
            y = ny
            turn_times = 0
        else:
            break

print(count)


    
