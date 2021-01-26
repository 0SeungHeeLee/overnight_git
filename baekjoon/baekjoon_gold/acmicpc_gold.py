# map_size,dot_size=map(int,input().split())
# dot_infR=[0]*(map_size+1)
# dot_infC=[0]*(map_size+1)
# dot_scoreR=[0]*(map_size+1)
# dot_scoreC=[0]*(map_size+1)
# for i in range(dot_size):
#     a,b=map(int,input().split())
#     dot_infR[a]+=1
#     dot_infC[b]+=1

# for i in range(1,map_size+1):
#     for j in range(1,map_size+1):
#         dot_scoreR[i]+=abs(i-j)*dot_infR[j]
#         dot_scoreC[i]+=abs(i-j)*dot_infC[j]

# dot_scoreR[0]=999999999
# dot_scoreC[0]=999999999
# print(min(dot_scoreR)+min(dot_scoreC))


# #15683
# import sys
# sys.setrecursionlimit(100000)
# size_row,size_col=map(int,input().split())
# map_inf=[]
# cam_inf=[]
# val_min=65
# for i in range(size_row):map_inf.append(list(map(int,input().split())))

# def cal_count(arr,key):
#     global size_row
#     global size_col
#     cnt=0
#     for i in range(size_row):
#         for j in range(size_col):
#             if arr[i][j]==key:cnt+=1
#     return cnt

# for i in range(size_row):
#     for j in range(size_col):
#         if map_inf[i][j]>0 and map_inf[i][j]<6:cam_inf.append([i,j,map_inf[i][j]])
# val_spc=cal_count(map_inf,0)
# dir_inf=[[1,0],[0,-1],[-1,0],[0,1]]
# dir_mod=[]
# dir_mod.append([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
# dir_mod.append([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
# dir_mod.append([[1,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,1]])
# dir_mod.append([[1,1,0,0],[0,1,1,0],[0,0,1,1],[1,0,0,1]])
# dir_mod.append([[1,1,1,0],[0,1,1,1],[1,0,1,1],[1,1,0,1]])
# dir_mod.append([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]])
# dir_cam=[0]*8

# def task_find(dp):
#     global map_inf
#     global cam_inf
#     global dir_inf
#     global dir_mod
#     global dir_cam
#     global val_min
#     global val_spc
#     global size_row
#     global size_col

#     if dp==len(cam_inf):
#         map_chk=[[False]*size_col for _ in range(size_row)]
#         for i in range(len(cam_inf)):
#             lR=cam_inf[i][0]
#             lC=cam_inf[i][1]
#             cV=map_inf[lR][lC]  #캠 종류
#             cD=dir_cam[i]       #캠 방향
#             for j in range(4):
#                 if dir_mod[cV][cD][j]==True:
#                     cnt=0
#                     while True:
#                         cnt+=1
#                         mR=lR+cnt*dir_inf[j][0]
#                         mC=lC+cnt*dir_inf[j][1]
#                         if mR<0 or mC<0 or mR>=size_row or mC>=size_col:break
#                         if map_inf[mR][mC]==6:break
#                         if map_inf[mR][mC]>0:continue
#                         map_chk[mR][mC]=True;
#         tmp_min=val_spc-cal_count(map_chk,True)
#         if val_min>tmp_min:val_min=tmp_min
#     else:
#         for i in range(4):
#             dir_cam[dp]=i
#             task_find(dp+1)
#             if cam_inf[dp][2]==2 and i==1:break
#             if cam_inf[dp][2]==5 and i==0:break
# task_find(0)
# print(val_min)

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