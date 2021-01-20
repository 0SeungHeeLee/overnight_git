# #1103(pypy3)
# import sys
# sys.setrecursionlimit(100000)
# size_row,size_col=map(int,input().split())
# inf_map=[]
# for i in range(size_row):inf_map.append(input())
# inf_dir=[[1,0],[-1,0],[0,1],[0,-1]]
# chk_map=[[False]*size_col for _ in range(size_row)]
# chk_max=[[0]*size_col for _ in range(size_row)]
# dp_max=0
# dp_cut=size_row*size_col

# def case_circulation():
#     print(-1)
#     sys.exit()

# def find_max(lR,lC,dp):
#     global size_row
#     global size_col
#     global chk_map
#     global chk_max
#     global inf_map
#     global inf_dir
#     global dp_max
#     global dp_cut

#     if dp_max<dp:dp_max=dp
#     chk_max[lR][lC]=dp
#     keyInt=int(inf_map[lR][lC])

#     for i in range(4):
#         mR=lR+keyInt*inf_dir[i][0]
#         mC=lC+keyInt*inf_dir[i][1]
#         if mR<0 or mC<0 or mR>=size_row or mC>=size_col:continue
#         if inf_map[mR][mC]=='H':continue
#         if chk_map[mR][mC]==True:case_circulation()
#         if dp+1<=chk_max[mR][mC]:continue
#         chk_map[mR][mC]=True
#         find_max(mR,mC,dp+1)
#         chk_map[mR][mC]=False

# chk_map[0][0]=True
# find_max(0,0,1)
# print(dp_max)

# #1987(pypy3)
# import sys
# size_row,size_col=map(int,input().split())
# inf_map=[list(map(lambda x:ord(x)-65,input())) for i in range(size_row)]
# chk_alp=[False]*100
# inf_dir=[[0,1],[0,-1],[1,0],[-1,0]]
# ans_max=0

# def find_max(lR,lC,tM):
#     global size_row
#     global size_col
#     global inf_dir
#     global ans_max
#     global inf_map
#     global chk_alp

#     if ans_max<tM:
#         ans_max=tM
#         if ans_max==26:
#             print(ans_max)
#             sys.exit()

#     for i in range(4):
#         mR=lR+inf_dir[i][0]
#         mC=lC+inf_dir[i][1]
#         if mR<0 or mC<0 or mR>=size_row or mC>=size_col:continue
#         if chk_alp[inf_map[mR][mC]]==True:continue

#         chk_alp[inf_map[mR][mC]]=True
#         find_max(mR,mC,tM+1)
#         chk_alp[inf_map[mR][mC]]=False

# chk_alp[inf_map[0][0]]=True
# find_max(0,0,1)
# print(ans_max)

# #17142
# from itertools import combinations
# map_size,virus_active=map(int,input().split())
# map_inf=[]
# virus_inf=[]
# for i in range(map_size):
#     map_inf.append([])
#     map_inf[i]=list(map(int,input().split()))
# for i in range(map_size):
#     for j in range(map_size):
#         if map_inf[i][j]==2:
#             virus_inf.append([i,j])

# db_dir=[[0,1],[0,-1],[1,0],[-1,0]]
# virus_idx=[]
# for i in combinations(virus_inf,virus_active):virus_idx.append(i)
# time_min=map_size*map_size

# def task_find(map,size):
#     global time_min
#     global db_dir

#     ed=0
#     stair=[]
#     queue=[]
#     check=[[0 for i in range(size)] for j in range(size)]
#     for i in range(size):
#         for j in range(size):
#             if map[i][j]==3:
#                 queue.append([])
#                 queue[len(queue)-1].append(i)
#                 queue[len(queue)-1].append(j)
#                 check[i][j]=1
#                 stair.append(0)
#     while len(queue)>ed:
#         for i in range(4):
#             mi=queue[ed][0]+db_dir[i][0]
#             mj=queue[ed][1]+db_dir[i][1]
#             if mi<0 or mj<0 or mi>=size or mj>=size:continue
#             if map[mi][mj]==1:continue
#             if check[mi][mj]>0:continue
#             queue.append([])
#             queue[len(queue)-1].append(mi)
#             queue[len(queue)-1].append(mj)
#             check[mi][mj]=1
#             stair.append(stair[ed]+1)
#         ed+=1
#     for i in range(size):
#         for j in range(size):
#             if map[i][j]!=1 and check[i][j]==0:return
#     cnt=ed-1
#     while cnt>=0:
#         if map[queue[cnt][0]][queue[cnt][1]]!=2:break
#         cnt-=1
#     tmp_min=stair[cnt]
#     if tmp_min<time_min:time_min=tmp_min

# for i in range(len(virus_idx)):
#     for j in range(len(virus_idx[0])):
#         map_inf[virus_idx[i][j][0]][virus_idx[i][j][1]]=3
#     task_find(map_inf,map_size)
#     for j in range(len(virus_idx[0])):
#         map_inf[virus_idx[i][j][0]][virus_idx[i][j][1]]=2

# if time_min<map_size*map_size:print(time_min)
# else:print(-1)