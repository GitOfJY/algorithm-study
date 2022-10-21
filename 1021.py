'''
# section2.2 K번째 수

import sys
sys.stdin = open("input.txt", "rt")
test = int(input())

for x in range(test):
    
    list = []
    tlist = []

    n, s, e, k = map(int, input().split())
    
    # 3번째 줄을 입력 받아야 하는데 n개로 계속 바뀜
    # 변수를 설정하고 거기에 값을 저장해야해서 for문을 어떻게 돌릴지 모르겠음
    # map을 이용해서 바로 list에 넣을 수 있는지?

    # 방법1. 한 줄 입력이지만 for문으로 개별 값 받기 > 실패
    #for i in range(n):
    #    list.append(int(input()))
    # ValueError: invalid literal for int() with base 10: '5 2 7 3 8 9'
    
    # 방법2. map으로 받은 것 바로 append 해보기 > 실패
    #list = list.append(map(int, input().split()))
    # AttributeError: 'NoneType' object has no attribute 'append'

    # 방법3. 스트링으로 받고 split으로 끊고 리스트 담기 > 성공
    str = input()
 
    #print(str)
    #5 2 7 3 8 9
        
    list.append(str.split(" "))   
    #print(list)
    # [['5', '2', '7', '3', '8', '9']]

    for i in range(s-1, e):
        tlist.append(int(list[0][i]))
    # print(tlist)
    # [2, 7, 3, 8]
    
    tlist.sort()
    print('#',x+1,' ',tlist[k-1])


import sys
sys.stdin = open("input.txt", "rt")
T = int(input())

for t in range(T):
    n, s, e, k = map(int, input().split())

    # a라는 list 생성하지 않고 map으로 받고 list 생성
    a = list(map(int, input().split()))
    # print(a)
    # [5, 2, 7, 3, 8, 9]

    # 인덱스 이용해서 원하는 부분 추출 가능
    a = a[s-1:e]
    # print(a)
    # [2, 7, 3, 8]
    a.sort()
    print("#%d %d" %(t+1, a[k-1]))


    

# section2.3 K번째 큰 수
import sys
sys.stdin = open("input.txt", "rt")
N, k = map(int, input().split())
a = list(map(int, input().split()))
b = []

# 2중 for문 사용
#for x in range(N-2):  
#    sum = 0
    #for y in range(3):
        #sum += a[x]
        #TypeError: unsupported operand type(s) for +=: 'builtin_function_or_method' and 'int'
        #print(a[x])
        #print(type(a[x]))
    #    sum += a[x]
    #    x += 1
#    b.append(sum)
#b.sort()
#print(b)
# [62, 70, 72, 79, 102, 109, 133, 143]
# 모든 경우의 수가 안 나옴


# 3중 for문 사용
for x in range(N-2):
    #print("x ",x)  
    for y in range(x+1, N-1):
        #print("y ",y) 
        for z in range(y+1, N):
            #print("z ",z) 
            sum = a[x] + a[y] + a[z]
            b.append(sum)
            
            #print(a[x], a[y], a[z])
            #print(sum)
            #print(' ')
            
            sum = 0

b = list(set(b))
b.sort(reverse=True)
print(b[k-1])
# 143
'''


import sys
sys.stdin = open("input.txt", "rt")
n, k = map(int, input().split())
a = list(map(int, input().split()))
res = set()
# 중복 제거하기 위한 set

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])
res = list(res)
res.sort(reverse=True)
print(res[k-1])



'''
# 최솟값 구하기
arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = float('inf') # 파이썬에서 가장 큰 값 초기화
for i in range(len(arr)):
    if arr[i] < arrMin:
        arrMin = arr[i]
print(arrMin)   

arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = arr[0]
for i in range(1, len(arr)):
    if arr[i] < arrMin:
        arrMin = arr[i]
print(arrMin)

arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = float('inf')
for i in arr:
    if arr[i] < arrMin:
        arrMin = arr[i]
print(arrMin) 
'''


















