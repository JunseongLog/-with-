# 내 풀이
# 행, 열 입력 받기
n, m = map(int, input().split())

# 리스트 입력 받으면서 저장
data = []
for i in range(n):
    data.append([])
    data[i] = list(map(int, input().split()))

# 행마다 가장 작은 수를 넣어줄 리스트
min_list = []

# 행에서 가장 작은 수를 리스트에 넣어줌
for i in range(n):
    min_list.append(min(data[i]))

# 가장 작은 수를 모아놓은 리스트 안에서 가장 큰 값을 출력
max_number = max(min_list)
print(max_number)


"""
# 책 풀이 1
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)


# 책 풀이 2
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    
    result = max(min_value, result)

print(result)

"""