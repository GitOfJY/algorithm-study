'''

#section2.4 대표값

import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
scoreList = list(map(int, input().split()))
sList = []
avg = 0
min = float('inf')
maxIndex = 0
maxScore = -1


for i in range(n):
    avg += scoreList[i]
avg = round(avg/n)
#print(avg) 74

for j in range(n):

    if (scoreList[j] > avg):
        sList.append(scoreList[j] - avg)
    else:
        sList.append(avg - scoreList[j])

    if sList[j] < min:
        min = sList[j]
    
#print(min) 1
#print(sList) [29, 1, 8, 13, 18, 7, 1, 5, 1, 6]

for z in range(n):
    if sList[z]==min:
        if scoreList[z] > maxScore:
            maxScore = scoreList[z]
            maxIndex = z

print("%d %d" %(avg, maxIndex+1))



#section2.5 정다면체
import sys
sys.stdin = open("input.txt", "rt")
n, m = map(int, input().split())
sumList = []
cnt = 0
fList = []

for i in range(n):
    for j in range(m):
        sumList.append(i+j+2)

for x in range(n+m+1):
    for y in sumList:
        if x == y:
            cnt += 1   
    fList.append([cnt, x])
    cnt=0

for x in range(len(fList)):
    if fList[x][0] == max(fList)[0]:
        print(x, end=' ')

        

import sys
sys.stdin = open("input.txt", "rt")
n, m = map(int, input().split())
cnt = [0]*(n+m+3)
max = -2147000000

for i in range(1,n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1

for i in range(n+m+1):
    if cnt[i] > max:
        max = cnt[i]

for i in range(n+m+1):
    if cnt[i]==max:
        print(i, end=' ')



#section2.6 자릿수의 합
import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
nList = list(map(str, input().split()))
cntList = [0]*n
max = -247000000


이중 for문 사용, cnt 리스트
1 for문 > nlist 하나씩 접근
        > 2 for문 
                  > len으로 자리수 합 구하기, cnt리스트에 넣기
cnt리스트 중 max 구하고 숫자 출력

def digit_sum(x):
    sum = 0
    for i in range(len(x)):
        sum += int(x[i:i+1])
    return sum

for i in range(n):
    cntList[i] += digit_sum(nList[i])

for i in range(n):
    if max < cntList[i]:
        max = cntList[i]

for i in range(n):
    if max == cntList[i]:
        print(nList[i])
        break

sol1.
import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
a = list(map(int, input().split()))
max = -214700000

def digit_sum(x):
    sum=0
    while x>0:
        sum+=x%10
        x=x//10
    return sum

for x in a:
    tot=digit_sum(x)
    if tot>max:
        max=tot
        res=x
print(res)

sol2.
def digit_sum(x):
    sum=0
    for i in str(x):
        sum += int(i)
    return sum
        
'''
