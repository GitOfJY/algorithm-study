'''
#곳감(모래시계)
import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
list1 = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
list2 = [list(map(int, input().split())) for _ in range(m)]
# EOFError: EOF when reading a line
# EOF (End Of File)로 input을 사용한 입력 시 더이상 입력할 파일이 없다는 뜻


for i in range(m):
    
    rownum = list2[i][0]
    direcnum = list2[i][1]
    circlenum = list2[i][2]

    if direcnum == 0:
        # 왼쪽 회전
        for j in range(circlenum):
            list1[rownum-1].insert(n, list1[rownum-1][0])
            list1[rownum-1].pop(0)
    else:
        # 오른쪽 회전
        for j in range(circlenum):
            list1[rownum-1].insert(0, list1[rownum-1][n-1])
            list1[rownum-1].pop()

sumlist = 0

for i in range(n//2+1):
    if i == n//2:
        sumlist += list1[i][n//2]
    else:
        sumlist += sum(list1[i][0+i:n-i])
        sumlist += sum(list1[n-1-i][0+i:n-i])

print(sumlist)



import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

for i in range(m):
    h, t, k = map(int, input().split())
    if t == 0:
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())

res = 0
s = 0
e = n-1
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(res)





# 봉우리
import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
mlist = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

for i in range(n):
    mlist[i].insert(0, 0)
    mlist[i].insert(n+1, 0)

addzero = [0 for i in range(n+2)]
mlist.insert(0, addzero)
mlist.insert(n+1, addzero)

for x in range(1, n+1):
    for y in range(1, n+1):
        if mlist[x][y] > mlist[x-1][y] and mlist[x][y] > mlist[x][y-1] and mlist[x][y] > mlist[x][y+1] and mlist[x][y] > mlist[x+1][y]:
            cnt += 1

print(cnt)
'''
import sys
sys.stdin = open("input.txt", "rt")
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0]*n)
a.append([0]*n)

for x in a:
    x.insert(0, 0)
    x.append(0)

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1
print(cnt)
