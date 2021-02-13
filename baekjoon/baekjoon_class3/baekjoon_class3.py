#1074
import sys

map_size, obj_locR, obj_locC = map(int, sys.stdin.readline().split())

val_size=2**map_size
def search(locR,locC,size,val):
    global obj_locR
    global obj_locC

    if size == 1:
        print(val)
        sys.exit(0)

    max_val = size**2
    val_db = [val, val+int(max_val/4), val+int(max_val/2), val+int(max_val/4*3)]
    loc_add = int(size/2)

    if obj_locR < locR + loc_add and obj_locC < locC + loc_add:
        search(locR, locC, loc_add, val_db[0])
    elif obj_locR < locR + loc_add and obj_locC >= locC + loc_add:
        search(locR, locC + loc_add, loc_add, val_db[1])
    elif obj_locR >= locR + loc_add and obj_locC < locC + loc_add:
        search(locR + loc_add, locC, loc_add, val_db[2])
    else:
        search(locR + loc_add, locC + loc_add, loc_add, val_db[3])

search(0,0,val_size,0)

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