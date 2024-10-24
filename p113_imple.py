# 입력 받기
n = int(input())

count = 0
# 시간, 분, 초를 하나씩 올리면서 완전 탐색하는 거라서 3중 반복문을 씀
# n이 23이라도 하루는 86,400초이므로 완전탐색을 하더라도 10만번도 연산이 되지 않으므로 완전 탐색 가능.
for h in range(n + 1):
    for m in range(60):
        for s in range(60):
            # 문자열을 더하면 문자열이 그냥 붙음.
            if '3' in str(h) + str(m) + str(s):
                count += 1

print(count)