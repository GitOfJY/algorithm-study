'''
#스토쿠 검사
행 / 열 / 3*3 체크
import sys
sys.stdin = open("input.txt", "rt")
chlist = [list(map(int, input().split())) for _ in range(9)]

def check(chlist):
    for x in range(9):
        olist = list(range(1, 10))
        rowlist = []
        collist = []
        
        for y in range(9):
            rowlist.append(chlist[x][y])
            collist.append(chlist[y][x])
         
        if sorted(rowlist) != olist or sorted(collist) != olist:
            print("NO")
            break
    else:
        for x in range(0, 9, 3):
            for y in range(0, 9, 3): 
                emlist = []
                
                for z in range(3): 
                    for k in range(3):
                        emlist.append(chlist[x+z][y+k])
                
                if sorted(emlist) != olist:
                    print("NO")
                    break

        print("YES")

check(chlist)



import sys
sys.stdin = open("input.txt", "rt")

def check(a):

    for i in range(9):
        ch1 = [0]*10
        ch2 = [0]*10
        for j in range(9):
            ch[a[i][j]] = 1
            ch[a[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False
    
    for i in range(3):
        for j in range(3):
            ch3 = [o]*10
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]] = 1
                if sum(ch3) != 9:
                    return False

    return Ture

a = [list(map(int, input().split())) for _ in range(9)]

if check(a):
    print("YES")
else:
    print("NO")







# 격자판 회문수
import sys
sys.stdin = open("input.txt", "rt")
chlist = [list(map(int, input().split())) for _ in range(7)]
cnt = 0

# 가로 검사 2개 
for x in range(7):  
    for y in range(3):
        for z in range(2): 
            if chlist[x][y+z] != chlist[x][y+4-z]:
                break
        else:
            cnt += 1

# 세로 검사
for x in range(3):
    for y in range(7):
        for z in range(2):
            if chlist[x+z][y] != chlist[x+4-z][y]:
                break
        else:
            cnt += 1

print(cnt)
'''
import sys
sys.stdin = open("input.txt", "rt")
board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0

for i in range(3):
    for j in range(7):
        tmp = board[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt += 1
        for k in range(2):
            if board[i+k][j] != board[i+5-k-1][j]:
                break
        else:
            cnt += 1
print(cnt)












