'''
# 카드 역배치
import sys
sys.stdin = open("input.txt", "rt")
list = []

for x in range(1, 21):
    list.append(x)

def change(x, y):
    for n in range((y - x + 1)//2): 
        tmpList = list[x-1+n] 
        list[x-1+n] = list[y-1-n] 
        list[y-1-n] = tmpList


for i in range(10):
    tmp = input().split()
    ai, bi = map(int, tmp)
    change(ai, bi)

print(*(list))

#파이썬 리스트 요소 한번에 출력하기 : print(*리스트이름)



# a,b = map(int, input().split())
# a, b = b, a
# 파이썬 스왑 방법

import sys
sys.stdin = open("input.txt", "rt")
a = list(range(21))
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]
a.pop(0)
for x in a:
    print(x, end=' ')





# 두 리스트 합치기
import sys
sys.stdin = open("input.txt", "rt")
n = input()
flist = list(map(int, input().split()))
m = input()
slist = list(map(int, input().split()))

result = []
result = flist + slist
print(*sorted(result))



import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
p1 = p2 = 0
c= []

while p1<n and p2<m:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1

if p1 < n:
    c = c + a[p1:]
if p2 < m:
    c = c + b[p2:]

for x in c:
    print(x,  end=' ')





# 수들의 합
import sys
sys.stdin = open("input.txt", "rt")
n, m = map(int, input().split())
list = list(map(int, input().split()))
# print(n, m, list)
# 8 3 [1, 2, 1, 3, 1, 1, 1, 2]
# 1개씩 합 구하고 2개씩 합 구하고 m개씩 합 구하기 > 코드는? > 2중 for문 사용


#for i in range(1, m+1):
#    for j in range(n-j):
        # 8개 2개일때 7번
        # 8개 3개일때 6번
        # 8개 4개일떄 5번
        #if 
        # 2개의 합 > 3개의 합 >> 이렇게 이어질때 합을 못 구하겠음
        # 리스트의 인덱싱 합이 있으면 가능할 것 같은데



import sys
sys.stdin = open("input.txt", "rt")
n, m = map(int, input().split())
a = list(map(int, input().split()))

lt = 0
rt = 1
tot = a[0]
cnt = 0

while True:
    if tot<m:
        if rt>n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1
print(cnt)





# 격자판 최대합
'''    
import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

# 가로합, 세로합, 대각선합을 따로 함수로 만들어서 구해야하나?

def sumHorizon(n):
    sum = 0


def sumVertical(n):
    sum = 0

def sumDiagonal(n):
    sum = 0
