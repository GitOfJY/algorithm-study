'''
# 격자판 최대합   
import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
# sum = 0
# maxSum = 0
# UnboundLocalError: local variable 'sum' referenced before assignment
# 가로합, 세로합, 대각선합을 따로 함수로 만들어서 구해야하나?


def sumHorizon(n):
    sum = 0
    maxSum = 0

    for i in range(n):
        for j in range(n):
            sum += arr[i][j]
            if (j == n-1):
                if maxSum < sum:
                    maxSum = sum
                    sum = 0
                else:
                    sum = 0
    return maxSum


def sumVertical(n):
    sum = 0
    maxSum = 0
    
    for i in range(n):
        for j in range(n):
            sum += arr[j][i]
            if (j == n-1):
                if maxSum < sum:
                    maxSum = sum
                    sum = 0
                else:
                    sum = 0
    return maxSum


def sumDiagonal(n):
    lsum = 0 
    rsum = 0 
    maxSum = 0
    
    for i in range(n):
        lsum += arr[i][i]
        rsum += arr[i][n-i-1]
    
        if (i == n-1):
                if maxSum < lsum:
                    maxSum = lsum
                    lsum = 0
                elif maxSum < rsum:
                    maxSum = rsum
                    rsum = 0
                else:
                    lsum = 0
                    rsum = 0

    return maxSum

result = max(sumDiagonal(5), sumVertical(5), sumHorizon(5))
print(result)
#print(sumDiagonal(5), sumVertical(5), sumHorizon(5))
# 155 149 154
# 각 출력값은 제대로 나오는데 채점 돌리면 틀렸다고 나옴


import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
largest = -2147000000

for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2
sum1 = sum2 = 0

for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2
print(largest)

    



# 사과나무(다이아몬드)
1(2) > 3(1.2.3) > 5(0.1.2.3.4) > 3(1.2.3) > 1(2)
1(4) > 3(3.4.5) > 5(2.3.4.5.6) > 7(1.2.3.4.5.6.7) > 5 > 3 > 1
 

import sys
#sys.stdin = open("input.txt", "rt")
n = int(input())
list = [list(map(int, input().split())) for _ in range(n)]
sumList = 0
# 리스트의 인덱싱을 사용하면 될 것 같다
#print(list[0][2:3])
#print(list[1][1:4])
#print(list[2][0:5])
#print(list[3][1:4])
#print(list[4][2:3])

for i in range(n//2+1):
    if i == n//2:
        sumList += sum(list[i][n//2-i:n//2+1+i])
    else:
        sumList += sum(list[i][n//2-i:n//2+1+i])
        sumList += sum(list[n-1-i][n//2-i:n//2+1+i])
        # TypeError: 'int' object is not callable
print(sumList)

'''

import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
res = 0
s = e = n//2
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(res)
