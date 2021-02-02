#1074
val_find,size_row,size_col=map(int,input().split())
def find_ans(x,y):
    global size_row
    global size_col

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