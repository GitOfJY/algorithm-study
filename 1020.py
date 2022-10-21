'''
# 빈리스트
a=[]
print(a)
b=list()
print(b)
# []
# []

# 리스트 생성
c=[1, 2, 3]
print(c)
print(c[0])
# [1, 2, 3]
# 1

d=list(range(1, 11))
print(d)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

f = c + d
print(f)
# [1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


c.append(6)
print(c)
# [1, 2, 3, 6]

c.insert(1, 8)
print(c)
# [1, 8, 2, 3, 6]
# 1번 인덱스에 8

c.pop()
print(c)
# 마지막 값 제거
# [1, 8, 2, 3]

c.pop(3)
print(c)
# 3번 인덱스 제거
# [1, 8, 2]

c.remove(8)
print(c)
# 해당 값 제거
# [1, 2]

print(c.index(2))
# 1
# c 리스트에서 해당 값의 인덱스 출력


a=list(range(1,11))
print(sum(a))
# 55
# a 리스트의 모든 값의 합 출력
print(max(a))
# 10
# a 함수의 최댓값 출력
print(min(a))
# 1
# a 함수의 최솟값 출력
print(min(7, 5))
# 5
# 인자 중 최솟값 출력



import random as r
a=list(range(1,11))
r.shuffle(a)
print(a)
# [10, 2, 1, 6, 9, 8, 5, 4, 7, 3]
a.sort()
print(a)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 오름차순
a.sort(reverse=True)
print(a)
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# 내림차순

a.clear()
print(a)
# []



a = [23, 12, 36, 53, 19]
print(a[:3])
# [23, 12, 36]
# 리스트 슬라이스, 0번 인덱스부터 2번 인덱스까지 출력
print(a[1:4])
# [12, 36, 53]

print(len(a))
# 5
# 리스트의 길이

# 리스트의 값 하나씩 접근하기
for i in range(len(a)):
    print(a[i], end=' ')
print()
# 23 12 36 53 19

for x in a:
    print(x, end=' ')
print()
# 23 12 36 53 19

for x in a:
    if x%2==1:
        print(x, end=' ')
print()
# 23 53 19 
# 홀수만 출력

for x in enumerate(a):
    print(x)
# (0, 23)
# (1, 12)
# (2, 36)
# (3, 53)
# (4, 19)
# 인덱스와 리스트의 원소 튜플형태로 출력

for x in enumerate(a):
    print(x[0], x[1])
print()
# 0 23
# 1 12
# 2 36
# 3 53
# 4 19

for index, value in enumerate(a):
    print(index, value)
print()
# 0 23
# 1 12
# 2 36
# 3 53
# 4 19
# enumerate는 이런 형태로 많이 사용함

#튜플 생성
b = (1, 2, 3, 4, 5)
print(b[0])
# 1
# b[0] = 7
# TypeError: 'tuple' object does not support item assignment
# 튜플값은 변경 불가


# a = [23, 12, 36, 53, 19]
if all(60>x for x in a):
    print("YES")
else:
    print("NO")
# YES
# 조건 모두가 참

if all(50>x for x in a):
    print("YES")
else:
    print("NO")
# NO
# 조건 중 1개만 거짓이어도 거짓

if any(15>x for x in a):
    print("YES")
else:
    print("NO")
# YES
# 조건 중 1개라도 참이면 참
# 모두가 거짓일때 거짓



a = [0]*3
print(a)
# [0, 0, 0]
# 크기가 3인 0으로 초기화된 1차원 리스트

a = [[0]*3 for _ in range(3)]
print(a)
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# 2차원 리스트 생성

a[0][1] = 1
a[1][1] = 2
print(a)
# [[0, 1, 0], [0, 2, 0], [0, 0, 0]]

for x in a:
    print(x)
# [0, 1, 0]
# [0, 2, 0]
# [0, 0, 0]

for x in a:
    for y in x:
        print(y, end=' ')
    print()
# 0 1 0 
# 0 2 0 
# 0 0 0 


def add(a, b):
    c=a+b
    print(c)
    
add(3, 2)
# 5

def add(a,b):
    c=a+b
    return c

print(add(5, 8))
# 13
# return은 함수의 종료 의미도 있음

def add(a,b):
    c=a+b
    d=a-b
    return c, d

print(add(5, 1))
# (6, 4)
# 튜플 형태로 여러개의 값을 return



def isPrime(x):
    for i in range(2, x):
        if x%i==0:
            return False
    return True

a=[12, 13, 7, 9, 19]
for x in a:
    if isPrime(x):
        print(x, end=' ')
# 13 7 19 
# 소수만 출력
'''


def plus_one(x):
    return x+1
print(plus_one(1))
#2

plus_two = lambda x: x+2
print(plus_two(1))
# 3
# plus_two는 변수명

# 람다함수는 내장함수의 인자로 사용할때 편리
a=[1, 2, 3]
print(list(map(plus_one, a)))
print(list(map(lambda x: x+1, a)))
# [2, 3, 4]




import sys
sys.stdin = open("input.txt", "rt")
n, k = map(int, input().split())
list = []

for i in range(1, n+1):
    if n%i == 0:
        list.append(i)

if len(list) < k:
    print(-1)
else:
    print(list[k-1])

    

'''

import sys
sys.stdin = open("input.txt", "rt")
n, k = map(int, input().split())
cnt = 0
for i in range(1, n+1):
    if n%i==0:
        cnt+=1
    if cnt==k:
        print(i)
        break
else:
    print(-1)

'''































