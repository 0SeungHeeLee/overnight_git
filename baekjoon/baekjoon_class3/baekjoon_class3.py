#9019
import sys
case_len=int(sys.stdin.readline())

#def chk_same(x):
#    k=x[0]
#    for i in x:
#        if i!=k:return False
#    return True

for _ in range(case_len):
    val_now,val_obj=map(int,sys.stdin.readline().split())
    stair=['']
    data=[val_now]
    loc=[-1]
    chk=[False]*10000
    st=0
    ed=-1

    while True:
        ed+=1
        if val_obj==data[ed]:
            ans=[]
            while ed>=0:
                ans.append(stair[ed])
                ed=loc[ed]
            ans_len=len(ans)-1
            for i in range(ans_len,-1,-1):print(ans[i],end='')
            print()
            break
        if chk[data[ed]]==True:continue
        chk[data[ed]]=True

        #D
        d_num=data[ed]*2
        if d_num>9999:d_num-=10000
        st+=1
        stair.append('D')
        data.append(d_num)
        loc.append(ed)
        #S
        s_num=data[ed]-1
        if s_num<0:s_num=9999
        st+=1
        stair.append('S')
        data.append(s_num)
        loc.append(ed)
        #if chk_same(data[ed]):continue
        #L
        st+=1
        l_num=data[ed]
        if l_num<1000:l_num*=10
        else:
            tmp=int(l_num/1000)
            l_num-=tmp*1000
            l_num=l_num*10+tmp
        stair.append('L')
        data.append(l_num)
        loc.append(ed)
        #R
        st+=1
        r_num=data[ed]
        tmp=r_num%10
        r_num=int(r_num/10)
        r_num+=tmp*1000
        stair.append('R')
        data.append(r_num)
        loc.append(ed)

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