# 각각의 변수 입력 받기
n, m, k = map(int, input().split())
# 리스트 입력 받기
data = list(map(int, input().split()))

#데이터 정렬
data.sort()
# 오름차순으로 정렬되었기 때문에 마지막 값이 가장 큰 수, 뒤에서 두번째 값이 두번째로 큰 수임
max1 = data[n - 1]
max2 = data[n - 2]

# 가장 큰 수 max1이 더해지는 횟수 구하기
count = m / (k+1) * k # 큰 수가 더해지는 횟수
count = count + (m % (k+1)) # "m % (k+1)"이 완전히 나누어 떨어지지 않을때 나머지 값만큼 큰 수를 더해주기 때문에 나머지 값도 더해줌.

result = 0
result = result + (count * max1)
result = result + ((m - count) * max2) # max2가 더해지는 횟수는 전체 횟수인 m에서 큰 수가 더해지는 횟수인 count를 빼주면 됨.

# 이해 안되거나 자세한 풀이가 필요하면 page95에 정리해뒀음.