#소수 (에라토스테네스 체)
import sys
sys.stdin = open("input.txt", "rt")
n = int(input())

for x in range(3, n+1):
    for y in range(2, x):
        if x%y == 0:
            break
        
# 소수 > 다른 숫자로 나눴을 때 무조건 나머지가 남음
# for문에서 break하고 나가는 것을 모르겠음
# n을 받고 리스트를 만든 다음에 소수가 아니면 pop하는 방법 밖에 모르겠다


import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
ch = [0]*(n+1)
cnt = 0

for i in range(2, n+1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n+1, i):
            ch[j] = 1
print(cnt)





# 뒤집은 소수
import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
temp = ''
nList = list(map(int, input().split()))
print(nList)


def reverse(x):
    for i in range(len(str(x))//2):
        temp = x[i] 
        x[i] = x[-(i+1)]
        x[-(i+1)] = temp
        # TypeError: 'int' object is not subscriptable

print(reverse(1234))



import sys
sys.stdin = open("input.txt", "rt")

def reverse(x):
    res = 0
    while x>0:
        t = x % 10
        res = res*10 + t
        x = x // 10
    return res

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2+1):
        if x%i==0:
            return False
    else:
        return True


n = int(input())
a = list(map(int, input().split()))

for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')


'''

import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
cnt = 0

for x in range(3, n+1):
    for y in range(2, x):
        if x%y == 0:
            break
    else: 
        print(x, y, x%y)
        cnt += 1
print(cnt+1)
