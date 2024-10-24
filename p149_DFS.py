# 연결된 요소를 확인하는 대표적인 DFS유형임.
# ice_map의 행렬 크기 받기
n, m = map(int, input().split())

# ice_map 입력 받기 - 공백 없이 받기 때문에 split()제외
ice_map = []
for i in range(n):
    ice_map.append(list(map(int, input())))

def dfs(x, y):
    # 범위를 벗어나는 것은 제외 - 인덱스가 0부터 n-1까지, 0부터 m-1까지니까
    if (x >= n or x <= -1 or y >= m or y <= -1):
        return False
    
    # 방문된 곳이 아니라면 방문 처리 및 주변 노드 dfs로 방문처리하기
    if (ice_map[x][y] == 0):
        # 방문처리
        ice_map[x][y] = 1
        # 상-하-좌-우 dfs돌려서 주변에 상하좌우로 연결된 노드도 모두 방문처리 해주기
        # 4개 밖에 없어서 4번만 돌리는 것 같지만, (x-1, y)좌표로 가서도, 
        # 재귀함수의 특성으로 인해서 그 좌표 기준으로 상하좌우를 또 방문 처리하고 확인을 할거임.
        # 한번의 호출로 연결 되어있는 하나의 덩이는 모두 방문처리됨.
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        # 리턴 트루는 상하좌우로 dfs하는 것과는 상관없음. 4개의 dfs가 모두 return이 False여도 트루르 리턴함.
        # 그냥 방문하지 않은 칸(if문을 통과하면)이면 방문을 하고 리턴을 트루로 하는 거임. 한칸짜리 빈칸을 생각하면 이해하기 쉬움.
        return True
    # 범위를 벗어나지 않으면서, 이미 방문처리된 곳이나 칸막이가 있는 부분을 처리해주기 위한 리턴
    return False

#아이스크림을 카운트 하는 변수
result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)