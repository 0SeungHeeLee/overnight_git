# #1941
# import copy
# map_ver=[[0 for hor in range(4)] for ver in range(10)]
# map_hor=[[0 for hor in range(10)] for ver in range(4)]
# blk_dir=[[0,0],[0,0],[0,1],[1,0]]
# val_score=0

# def set_blkInf(cs,x,y,blk):
#     global blk_dir

#     blk.append([])
#     blk[0].append(x)
#     blk[0].append(y)
#     blk.append([])
#     blk[1].append(x+blk_dir[cs][1])
#     blk[1].append(y+blk_dir[cs][0])
# def cal_sumHor(x):
#     global map_hor
#     tmp=0
#     for i in range(4):tmp+=map_hor[i][x]
#     return tmp
# def cal_blk():
#     global map_ver
#     global map_hor
#     cnt_blk=0

#     for i in range(6,10):
#         for j in range(4):
#             if map_ver[i][j]>0:cnt_blk+=1
#             if map_hor[j][i]>0:cnt_blk+=1
    
#     return cnt_blk
        
# def chk_outRange():
#     global map_ver
#     global map_hor

#     chkV=[sum(map_ver[5]),sum(map_ver[4])]
#     chkH=[cal_sumHor(5),cal_sumHor(4)]
#     if chkV[1]>0:cntV=2
#     elif chkV[0]>0:cntV=1
#     else:cntV=0
#     if chkH[1]>0:cntH=2
#     elif chkH[0]>0:cntH=1
#     else:cntH=0

#     if cntV>0:
#         for i in range(9-cntV,9-cntV-6,-1):
#             for j in range(4):map_ver[i+cntV][j]=map_ver[i][j]
#     if cntH>0:
#         for i in range(9-cntH,9-cntH-6,-1):
#             for j in range(4):map_hor[j][i+cntH]=map_hor[j][i]

# def chk_getScore():
#     global map_ver
#     global map_hor
#     global val_score
    
#     while True:
#         chk_get=False
#         for i in range(9,5,-1):
#             for j in range(4):
#                 if map_ver[i][j]==0:break
#                 if j==3:
#                     val_score+=1
#                     for k in range(4):map_ver[i][k]=0
#                     chk_get=True              
#         if chk_get==False:break

#         for i in range(8,3,-1):
#             c2_chk=[]
#             for j in range(4):
#                 if map_ver[i][j]==0:continue
#                 if map_ver[i][j]==2:c2_chk.append(j)
#                 else:
#                     lY=i
#                     while lY+1<10 and map_ver[lY+1][j]==0:
#                         map_ver[lY+1][j]=map_ver[lY][j]
#                         map_ver[lY][j]=0
#                         lY+=1
#             if len(c2_chk)==0:continue
#             lY=i
#             chk_crash=True
#             while chk_crash:
#                 if lY>=9:break
#                 for j in c2_chk: 
#                     if map_ver[lY+1][j]>0:
#                         chk_crash=False
#                         break
#                 if chk_crash:
#                     for j in c2_chk: 
#                         map_ver[lY+1][j]=map_ver[lY][j]
#                         map_ver[lY][j]=0
#                     lY+=1

#     while True:
#         chk_get=False
#         for i in range(9,5,-1):
#             for j in range(4):
#                 if map_hor[j][i]==0:break
#                 if j==3:
#                     val_score+=1
#                     for k in range(4):map_hor[k][i]=0
#                     chk_get=True              
#         if chk_get==False:break

#         for i in range(8,3,-1):
#             c3_chk=[]
#             for j in range(4):
#                 if map_hor[j][i]==0:continue
#                 if map_hor[j][i]==3:c3_chk.append(j)
#                 else:
#                     lX=i
#                     while lX+1<10 and map_hor[j][lX+1]==0:
#                         map_hor[j][lX+1]=map_hor[j][lX]
#                         map_hor[j][lX]=0
#                         lX+=1
#             if len(c3_chk)==0:continue
#             lX=i
#             chk_crash=True
#             while chk_crash:
#                 if lX>=9:break
#                 for j in c3_chk: 
#                     if map_hor[j][lX+1]>0:
#                         chk_crash=False
#                         break
#                 if chk_crash:
#                     for j in c3_chk: 
#                         map_hor[j][lX+1]=map_hor[j][lX]
#                         map_hor[j][lX]=0
#                     lX+=1

# def act_blkDrop(blkV,blkH,blkC):
#     global map_ver
#     global map_hor

#     while blkV[1][1]<9 and map_ver[blkV[0][1]+1][blkV[0][0]]==0 and map_ver[blkV[1][1]+1][blkV[1][0]]==0:
#         blkV[0][1]+=1
#         blkV[1][1]+=1
#     while blkH[1][0]<9 and map_hor[blkH[0][1]][blkH[0][0]+1]==0 and map_hor[blkH[1][1]][blkH[1][0]+1]==0:
#         blkH[0][0]+=1
#         blkH[1][0]+=1
#     map_ver[blkV[0][1]][blkV[0][0]]=blkC
#     map_ver[blkV[1][1]][blkV[1][0]]=blkC
#     map_hor[blkH[0][1]][blkH[0][0]]=blkC
#     map_hor[blkH[1][1]][blkH[1][0]]=blkC

# num_block=int(input())
# for _ in range(num_block):
#     blk_case,blk_locY,blk_locX=map(int,input().split())
#     blk_infV=[]
#     set_blkInf(blk_case,blk_locX,blk_locY,blk_infV)
#     blk_infH=copy.deepcopy(blk_infV)

#     act_blkDrop(blk_infV,blk_infH,blk_case)
#     chk_getScore()
#     chk_outRange()

# print(val_score)
# print(cal_blk())

# #3954
# cnt_case=int(input())
# CODE_CNT_CUTLINE=50000000
# for _ in range(cnt_case):
#     size_db,size_code,size_input=map(int,input().split())
#     db_inf=[0]*size_db
#     code_inf=input()
#     input_inf=input()
#     point_db=0
#     point_code=0
#     point_input=0

#     dir_loopGOTO=[-1]*size_code
#     dir_loopPAIR=[]
#     for i in range(size_code):
#         if code_inf[i]=='[':
#             dir_loopPAIR.append(i)
#         if code_inf[i]==']':
#             tmp=len(dir_loopPAIR)-1
#             dir_loopGOTO[i]=dir_loopPAIR[tmp]
#             dir_loopGOTO[dir_loopPAIR.pop()]=i

#     for _ in range(CODE_CNT_CUTLINE):
#         if not point_code<size_code: break

#         if code_inf[point_code]=='-':
#             db_inf[point_db]-=1
#             if db_inf[point_db]<0:db_inf[point_db]=255

#         elif code_inf[point_code]=='+':
#             db_inf[point_db]+=1
#             if db_inf[point_db]>255:db_inf[point_db]=0

#         elif code_inf[point_code]=='<':
#             point_db-=1
#             if point_db<0:point_db=size_db-1

#         elif code_inf[point_code]=='>':
#             point_db+=1
#             if point_db>=size_db:point_db=0

#         elif code_inf[point_code]=='[':
#             if db_inf[point_db]==0:point_code=dir_loopGOTO[point_code]

#         elif code_inf[point_code]==']':
#             if db_inf[point_db]!=0:point_code=dir_loopGOTO[point_code]

#         elif code_inf[point_code]==',':
#             if point_input<size_input:
#                 db_inf[point_db]=ord(input_inf[point_input])
#                 point_input+=1
#             else:db_inf[point_db]=255
#         point_code+=1

#     if point_code>=size_code:
#         print('Terminates')
#         continue

#     bt_chk=[False]*size_code
#     for _ in range(CODE_CNT_CUTLINE):
#         if not point_code<size_code: break

#         if code_inf[point_code]=='-':
#             db_inf[point_db]-=1
#             if db_inf[point_db]<0:db_inf[point_db]=255

#         elif code_inf[point_code]=='+':
#             db_inf[point_db]+=1
#             if db_inf[point_db]>255:db_inf[point_db]=0

#         elif code_inf[point_code]=='<':
#             point_db-=1
#             if point_db<0:point_db=size_db-1

#         elif code_inf[point_code]=='>':
#             point_db+=1
#             if point_db>=size_db:point_db=0

#         elif code_inf[point_code]=='[':
#             if db_inf[point_db]==0:point_code=dir_loopGOTO[point_code]

#         elif code_inf[point_code]==']':
#             bt_chk[point_code]=True
#             if db_inf[point_db]!=0:point_code=dir_loopGOTO[point_code]

#         elif code_inf[point_code]==',':
#             if point_input<size_input:
#                 db_inf[point_db]=ord(input_inf[point_input])
#                 point_input+=1
#             else:db_inf[point_db]=255
#         point_code+=1
    
#     for i in range(size_code-1,-1,-1):
#         if bt_chk[i]==True:
#             bt_rng=i
#             break
#     val_ed=bt_rng
#     val_st=dir_loopGOTO[val_ed]
#     print("Loops "+str(val_st)+" "+str(val_ed))

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