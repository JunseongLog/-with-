# N 배열 크기 M 더하는 횟수 K 중복 가능 횟수

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

# 데이터 정렬
data.sort()

# K가 가장 작은 수인 1이여도 결국 두 가지 큰 숫자만 알고 이용하면 됨.
max = data[n - 1] # 가장 큰 수
max2 = data[n -2] # 두번째로 큰 수

sum = 0
count = 0

for i in range(m):
    if (m == 0):
        break
    
    if (count == k):
        sum += max2
        count = 0
        continue

    sum += max
    count += 1

print(sum)

