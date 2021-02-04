# #17255
# import sys
# a,b,n=map(int,sys.stdin.readline().split())
# db=[]
# for _ in range(n):
#     x,y,z=sys.stdin.readline().split()
#     db.append([int(x),str(y),int(z)])
# queueB=[]
# queueR=[]
# numB=[]
# numR=[]
# ansB=[]
# ansR=[]
# cnt_db=0
# cnt_gd=1
# val_time=0
# last_blue=-1
# last_red=-1

# def task_stk(arr,num,addV,limit):
#     global val_time
#     if len(arr)==0 or arr[len(arr)-1]+addV<=val_time:tmp=val_time
#     else:tmp=arr[len(arr)-1]
#     for _ in range(limit):
#         arr.append(tmp+addV)
#         num.append(tmp)
#         tmp+=addV
# def task_chk(chk,ans,addV):
#     global val_time
#     global cnt_gd
#     while len(chk)>0 and chk[0]==val_time:
#         ans.append(cnt_gd)
#         cnt_gd+=1
#         chk.pop(0)
# def task_del(chk):
#     global val_time
#     while len(chk)>0 and chk[0]==val_time:chk.pop(0)

# while cnt_db<n:
#     val_time+=1
#     if db[cnt_db][0]==val_time:
#         if db[cnt_db][1]=='B':task_stk(queueB,numB,a,db[cnt_db][2])
#         else:task_stk(queueR,numR,b,db[cnt_db][2])
#         cnt_db+=1
#     task_chk(numB,ansB,a)
#     task_chk(numR,ansR,b)
#     task_del(queueB)
#     task_del(queueR)
#     # print(f'Now Time: {val_time}')
#     # print(queueB,numB,ansB)
#     # print(queueR,numR,ansR)
# while len(queueB)>0 or len(queueR)>0:
#     val_time+=1
#     if len(ansB)>0:task_chk(numB,ansB,a)
#     if len(ansR)>0:task_chk(numR,ansR,b)
#     if len(queueB)>0:task_del(queueB)
#     if len(queueR)>0:task_del(queueR)

# print(len(ansB))
# for i in ansB:print(i,end=' ')
# print(f'\n{len(ansR)}')
# for i in ansR:print(i,end=' ')

# #15688
# import sys
# n=int(sys.stdin.readline())
# m=[int(sys.stdin.readline()) for _ in range(n)]
# m.sort()
# for i in range(n):print(m[i])

# #1325
# import sys
# sys.setrecursionlimit(1000000)
# n,m=map(int,sys.stdin.readline().split())
# k=[]
# for _ in range(n+1):k.append([])
# ans=[0 for i in range(n+1)]
# delCase=[0 for i in range(n+1)]
# for _ in range(m):
#     subC,mainC=map(int,sys.stdin.readline().split())
#     k[mainC].append(subC)
#     delCase[mainC]=mainC
# tmp=set(delCase)
# caseInf=list(tmp)

# maxRoot=0
# def searchAns(chk,x):
#     global maxRoot
#     global k
#     maxRoot+=1
#     chk[x]=True
#     for i in range(len(k[x])):
#         if chk[k[x][i]]==False:searchAns(chk,k[x][i])
        
# for i in caseInf:
#     maxRoot=0
#     chk=[False for j in range(n+1)]
#     searchAns(chk,i)
#     ans[i]=maxRoot

# print(ans)

# maxAns=max(ans)
# for i in range(1,n+1):
#     if maxAns==ans[i]:print(i,end=' ')

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