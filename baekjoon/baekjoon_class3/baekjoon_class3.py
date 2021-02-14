#1927
import sys
heap_size=int(sys.stdin.readline())
heap_db=[0 for i in range(131072)]
heap_last=-1

def get_parentNod(x):
    return int((x-1)/2)
def get_childNod(x):
    return x*2+1,x*2+2
def get_minNod(L,R):
    global heap_db

    if heap_db[R] == 0: return L
    elif heap_db[L] == 0: return R
    elif heap_db[L] <= heap_db[R]: return L
    else: return R

for t in range(heap_size):
    x=int(sys.stdin.readline())

    if x==0:
        if heap_last==-1: print(0)
        else:
            print(heap_db[0])
            heap_db[0]=0
            heap_db[0], heap_db[heap_last] = heap_db[heap_last], heap_db[0]
            nodLoc_now=0
            heap_last -= 1
            while True:
                nodLoc_lt, nodLoc_rt = get_childNod(nodLoc_now)

                if nodLoc_lt>heap_last:break
                nodLoc_goto=get_minNod(nodLoc_lt,nodLoc_rt)
                if heap_db[nodLoc_now]<=heap_db[nodLoc_goto]:break

                heap_db[nodLoc_now],heap_db[nodLoc_goto]=heap_db[nodLoc_goto],heap_db[nodLoc_now]
                nodLoc_now=nodLoc_goto
        continue

    heap_last += 1
    heap_db[heap_last] = x
    nodLoc_now = heap_last
    while nodLoc_now>0:
        nodLoc_pt=get_parentNod(nodLoc_now)
        if heap_db[nodLoc_pt]<=heap_db[nodLoc_now]:break
        heap_db[nodLoc_pt],heap_db[nodLoc_now]=heap_db[nodLoc_now],heap_db[nodLoc_pt]
        nodLoc_now=nodLoc_pt

# #1780
# import sys
# paper_size=int(sys.stdin.readline())
# paper_db=[list(map(int,sys.stdin.readline().split())) for _ in range(paper_size)]
#
# val_sum=[0,0,0]
#
#
# def chk_same(locR,locC,size):
#     global paper_db
#
#     limR=locR+size
#     limC=locC+size
#     val_chk=paper_db[locR][locC]
#     for i in range(locR,limR):
#         for j in range(locC,limC):
#             if val_chk!=paper_db[i][j]:return False
#     return True
#
# def chk_use(locR,locC,size):
#     global val_sum
#     global paper_db
#
#     if size==1 or chk_same(locR,locC,size):
#         val_sum[paper_db[locR][locC]+1]+=1
#         return
#     val_addSize=int(size/3)
#     for i in range(0, size, val_addSize):
#         for j in range(0, size, val_addSize):
#             chk_use(locR+i, locC+j, val_addSize)
#
# chk_use(0,0,paper_size)
#
# for i in val_sum:print(i)

# #1697
# import sys
# loc_onezan,loc_ototo = map(int,sys.stdin.readline().split())
# bfs_loc=[loc_onezan]
# bfs_time=[0]
# bfs_chk=[False for _ in range(100001)]
# ed=-1
#
# while True:
#     ed+=1
#
#     if bfs_loc[ed]<0 or bfs_loc[ed]>100000:continue
#     if bfs_chk[bfs_loc[ed]]:continue
#     if bfs_loc[ed]==loc_ototo:break
#
#     bfs_chk[bfs_loc[ed]]=True
#     bfs_loc.append(bfs_loc[ed]+1)
#     bfs_time.append(bfs_time[ed]+1)
#     bfs_loc.append(bfs_loc[ed]-1)
#     bfs_time.append(bfs_time[ed]+1)
#     bfs_loc.append(bfs_loc[ed]*2)
#     bfs_time.append(bfs_time[ed]+1)
#
# print(bfs_time[ed])

# #1676
# import sys
# pac_len=int(input())
#
# val_2=0
# val_5=0
#
# for i in range(pac_len,1,-1):
#     cpy_i=i
#     while cpy_i%2==0:
#         cpy_i=int(cpy_i/2)
#         val_2+=1
#     while cpy_i%5==0:
#         cpy_i=int(cpy_i/5)
#         val_5+=1
#
# if val_5<val_2:val_2=val_5
# print(val_2)

# #1620
# import sys
# import copy
# mst_num, qst_num=map(int,sys.stdin.readline().split())
# mst_db=[]
# mst_dbSort=[[] for _ in range(mst_num)]
# for i in range(mst_num):
#     tmpStr=input()
#     mst_db.append(tmpStr)
#     mst_dbSort[i].append(tmpStr)
#     mst_dbSort[i].append(i)
#
# mst_dbSort = sorted(mst_dbSort,key=lambda x:x[0])
#
# for _ in range(qst_num):
#     getStr=input()
#     try: strToInt = int(getStr)
#     except: strToInt = None
#
#     if strToInt==None:
#         st=0
#         ed=mst_num-1
#         while st<=ed:
#             md=int((st+ed)/2)
#             if getStr==mst_dbSort[md][0]:
#                 print(mst_dbSort[md][1]+1)
#                 break
#             if getStr<mst_dbSort[md][0]:ed=md-1
#             else: st=md+1
#     else:print(mst_db[strToInt-1])


# #1541
# import copy
#
# def Asum(num,sign):
#     len_sign=len(sign)
#     val_sum=num[0]
#     for i in range(len_sign):
#         if sign[i]=='+':
#             val_sum+=num[i+1]
#         else:
#             val_sum-=num[i+1]
#
#     return val_sum
#
# db_str=input()
# len_str=len(db_str)
# loc_save=0
# db_num=[]
# db_sign=[]
# for i in range(len_str):
#     ord_str=ord(db_str[i])
#     if 48>ord_str or ord_str>57:
#         db_num.append(int(db_str[loc_save:i]))
#         db_sign.append(db_str[i])
#         loc_save=i+1
# db_num.append(int(db_str[loc_save:len_str]))
# len_num=len(db_num)
# len_sign=len(db_sign)
#
# for i in range(len_sign-1,-1,-1):
#     if db_sign[i]=='+':
#         db_num[i]+=db_num[i+1]
#         db_num.pop(i+1)
#         db_sign.pop(i)
# print(Asum(db_num,db_sign))

# #1074
# import sys
#
# map_size, obj_locR, obj_locC = map(int, sys.stdin.readline().split())
#
# val_size=2**map_size
# def search(locR,locC,size,val):
#     global obj_locR
#     global obj_locC
#
#     if size == 1:
#         print(val)
#         sys.exit(0)
#
#     max_val = size**2
#     val_db = [val, val+int(max_val/4), val+int(max_val/2), val+int(max_val/4*3)]
#     loc_add = int(size/2)
#
#     if obj_locR < locR + loc_add and obj_locC < locC + loc_add:
#         search(locR, locC, loc_add, val_db[0])
#     elif obj_locR < locR + loc_add and obj_locC >= locC + loc_add:
#         search(locR, locC + loc_add, loc_add, val_db[1])
#     elif obj_locR >= locR + loc_add and obj_locC < locC + loc_add:
#         search(locR + loc_add, locC, loc_add, val_db[2])
#     else:
#         search(locR + loc_add, locC + loc_add, loc_add, val_db[3])
#
# search(0,0,val_size,0)

# #1389
# import sys
# sys.setrecursionlimit(100000)
#
# relate_user, relate_size = map(int, sys.stdin.readline().split())
# user_val=relate_user+1
# relate_db = [[False for _ in range(user_val)] for _ in range(user_val)]
# for _ in range(relate_size):
#     input_valA, input_valB = map(int, sys.stdin.readline().split())
#     relate_db[input_valA][input_valB] = True
#     relate_db[input_valB][input_valA] = True
#
# ans_db=[0 for _ in range(user_val)]
# dps_chkVisit=[]
# def dps_search(nowLoc, dp):
#     global relate_db
#     global user_val
#     global dps_chkVisit
#
#     dps_chkVisit[nowLoc] = dp
#
#     for i in range(1,user_val):
#         if dps_chkVisit[i]>0 and dps_chkVisit[i]<=dp+1:continue
#         if relate_db[nowLoc][i]==False:continue
#
#         dps_search(i,dp+1)
#
# for user_num in range(1,user_val):
#     dps_chkVisit=[0 for _ in range(user_val)]
#     dps_search(user_num,1)
#     ans_db[user_num]=sum(dps_chkVisit)
#
# ans_db[0]=999999999
# print(ans_db.index(min(ans_db)))

# #9019
# import sys
# case_len=int(sys.stdin.readline())
#
# #def chk_same(x):
# #    k=x[0]
# #    for i in x:
# #        if i!=k:return False
# #    return True
#
# for _ in range(case_len):
#     val_now,val_obj=map(int,sys.stdin.readline().split())
#     stair=['']
#     data=[val_now]
#     loc=[-1]
#     chk=[False]*10000
#     st=0
#     ed=-1
#
#     while True:
#         ed+=1
#         if val_obj==data[ed]:
#             ans=[]
#             while ed>=0:
#                 ans.append(stair[ed])
#                 ed=loc[ed]
#             ans_len=len(ans)-1
#             for i in range(ans_len,-1,-1):print(ans[i],end='')
#             print()
#             break
#         if chk[data[ed]]==True:continue
#         chk[data[ed]]=True
#
#         #D
#         d_num=data[ed]*2
#         if d_num>9999:d_num-=10000
#         st+=1
#         stair.append('D')
#         data.append(d_num)
#         loc.append(ed)
#         #S
#         s_num=data[ed]-1
#         if s_num<0:s_num=9999
#         st+=1
#         stair.append('S')
#         data.append(s_num)
#         loc.append(ed)
#         #if chk_same(data[ed]):continue
#         #L
#         st+=1
#         l_num=data[ed]
#         if l_num<1000:l_num*=10
#         else:
#             tmp=int(l_num/1000)
#             l_num-=tmp*1000
#             l_num=l_num*10+tmp
#         stair.append('L')
#         data.append(l_num)
#         loc.append(ed)
#         #R
#         st+=1
#         r_num=data[ed]
#         tmp=r_num%10
#         r_num=int(r_num/10)
#         r_num+=tmp*1000
#         stair.append('R')
#         data.append(r_num)
#         loc.append(ed)

# #1764
# import sys
# fst_size,sec_size=map(int,sys.stdin.readline().split())
# fst_db=[sys.stdin.readline().rstrip() for _ in range(fst_size)]
# fst_db.sort()
# same_cnt=0
# same_db=[]
#
# for _ in range(sec_size):
#     sec_str=sys.stdin.readline().rstrip()
#     sec_len=len(sec_str)
#     st=0
#     ed=fst_size-1
#     while st<=ed:
#         md=int((st+ed)/2)
#         if sec_str==fst_db[md]:
#             same_cnt+=1
#             same_db.append(sec_str)
#             break
#         if sec_str<fst_db[md]:ed=md-1
#         else:st=md+1
# same_db.sort()
# print(same_cnt)
# for i in range(same_cnt):print(same_db[i])

# #1012
# val_case=int(input())
# inf_dir=[[1,0],[-1,0],[0,1],[0,-1]]

# def find_dps(dMap,dChk,sR,sC,r,c):
#     global inf_dir
#     dChk[r][c]=True
#     stk=[[r,c]]
#     ed=0
#     while len(stk)>ed:
#         lR=stk[ed][0]
#         lC=stk[ed][1]
#         for i in range(4):
#             mR=lR+inf_dir[i][0]
#             mC=lC+inf_dir[i][1]
#             if mR<0 or mC<0 or mR>=sR or mC>=sC:continue
#             if dMap[mR][mC]==False:continue
#             if dChk[mR][mC]==True:continue
#             stk.append([mR,mC])
#             dChk[mR][mC]=True
#         ed+=1

# def find_ans(db_map,sR,sC):
#     db_chk=[[False for j in range(sC)] for i in range(sR)]
#     cnt=0
#     for i in range(sR):
#         for j in range(sC):
#             if db_chk[i][j]==True:continue
#             if db_map[i][j]==False:continue
#             find_dps(db_map,db_chk,sR,sC,i,j)
#             cnt+=1
#     return cnt

# for _ in range(val_case):
#     size_col,size_row,cnt_place=map(int,input().split())
#     db_map=[[False for j in range(size_col)] for i in range(size_row)]
#     for _ in range(cnt_place):
#         x,y=map(int,input().split())
#         db_map[y][x]=True
#     print(find_ans(db_map,size_row,size_col))



# #1003
# val_case=int(input())
# chk=[0]*41
# chk[1]=1
# for i in range(2,41):chk[i]=chk[i-1]+chk[i-2]
# for _ in range(val_case):
#     val_goal=int(input())
#     if val_goal==0:print("1 0")
#     else:print(chk[val_goal-1],chk[val_goal])