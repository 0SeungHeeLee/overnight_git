#1325
import sys
sys.setrecursionlimit(1000000)
n,m=map(int,sys.stdin.readline().split())
k=[]
for _ in range(n+1):k.append([])
ans=[0 for i in range(n+1)]
delCase=[0 for i in range(n+1)]
for _ in range(m):
    subC,mainC=map(int,sys.stdin.readline().split())
    k[mainC].append(subC)
    delCase[mainC]=mainC
tmp=set(delCase)
caseInf=list(tmp)

maxRoot=0
def searchAns(chk,x):
    global maxRoot
    global k
    maxRoot+=1
    chk[x]=True
    for i in range(len(k[x])):
        if chk[k[x][i]]==False:searchAns(chk,k[x][i])
        
for i in caseInf:
    maxRoot=0
    chk=[False for j in range(n+1)]
    searchAns(chk,i)
    ans[i]=maxRoot

print(ans)

maxAns=max(ans)
for i in range(1,n+1):
    if maxAns==ans[i]:print(i,end=' ')

# #1103
# import sys
# sys.setrecursionlimit(1000000)
# num_size = list(map(int,input().split()))
# map_inf=[]
# for i in range(num_size[0]):map_inf.append(input())

# map_chk=[[0 for i in range(num_size[1])]for j in range(num_size[0])]
# val_max=0
# chk_add=[[0,1],[0,-1],[1,0],[1,-1]]

# def play_game(inf,chk,x,y,bx,by,cnt):
#     global num_size
#     global val_max
#     global chk_add

#     m=int(inf[y][x])
#     if chk[y][x]==1:
#         print("-1")
#         sys.exit()
#     chk[y][x]=1

#     for i in range(4):
#         mv=y+m*chk_add[i][0]
#         mh=x+m*chk_add[i][1]
#         if mv>=num_size[0] or mv<0 or mh>=num_size[1] or mh<0 or inf[mv][mh]=='H':
#             if val_max<cnt:val_max=cnt
#             continue
#         tmpChk = chk
#         play_game(inf,tmpChk,mh,mv,x,y,cnt+1)
# play_game(map_inf,map_chk,0,0,0,0,1)
# print(val_max)