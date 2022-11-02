'''
# 이분검색
import sys
sys.stdin = open("input.txt", "rt")
n, m = map(int, input().split())
list01 = list(map(int, input().split()))

for x in range(n):
    list01.sort()
    if list01[x] == m:
        print(x+1)
        break



import sys
sys.stdin = open("input.txt", "rt")
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
lt = 0
rt = n-1
while lt<=rt:
    mid = (lt + rt) // 2
    if a[mid] == m:
        print(mind+1)
        break
    elif a[mid] > m:
        rt = mid - 1
    else:
        lt = mid + 1





# 랜선 자르기(결정 알고리즘)
1. 랜선 길이를 다 더하고 필요한 갯수 만큼 나눈다
2. 길이로 총 갯수를 구하고 max라고 해 놓고 정수 값이니까 1씩 줄여간다


import sys
#sys.stdin = open("input.txt", "rt")
n, m = map(int, input().split())
list01 = []
num = 0

for _ in range(n):
    list01.append(int(input()))

max_length = sum(list01)//m

while (num!=m):
    for x in range(n):
        num += list01[x] // max_length
    if num != m:
        num = 0
        max_length -= 1

print(max_length)
# Time Limit Exceeded


'''











