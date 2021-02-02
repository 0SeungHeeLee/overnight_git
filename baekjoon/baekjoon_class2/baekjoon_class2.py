#18111
n,m,b=map(int,input().split())
t=[]
k=[]
for _ in range(n):t.append(list(map(int,input().split())))
for i in t:k+=i
n*=m
minL=min(k)
maxL=max(k)
ansT=99999999
ansL=-1
for tL in range(maxL,minL-1,-1):
    val_time=0
    val_block=b
    for i in range(n):
        tmp=k[i]-tL
        if tmp>0:
            val_time+=tmp*2
            val_block+=tmp
        else:
            val_time+=tmp*-1
            val_block+=tmp
    if val_block<0:continue
    if ansT>val_time:
        ansT=val_time
        ansL=tL
print(ansT,ansL)

# #15829
# n=int(input())
# s=input()
# k=[]
# for i in range(n):k.append(ord(s[i])-96)
# t=0
# for i in range(n):t+=k[i]*(31**i)
# t%=1234567891
# print(t)

# #11651
# n=int(input())
# k=[]
# for i in range(n):k.append(list(map(int,input().split())))
# k.sort(key=lambda x:x[0])
# k.sort(key=lambda x:x[1])
# for i in range(n):print(k[i][0],k[i][1])

# #10989
# import sys
# n=int(sys.stdin.readline())
# cnt=[0]*10001
# for i in range(n):cnt[int(sys.stdin.readline())]+=1
# for i in range(10001):
#     for j in range(cnt[i]):print(i)

# #10773
# k=int(input())
# a=[]
# for i in range(k):
#     t=int(input())
#     if t>0:a.append(t)
#     else:a.pop()
# print(sum(a))

# #7568
# val_size=int(input())
# arr=[]
# ans=[1]*val_size
# for i in range(val_size):arr.append(list(map(int,input().split())))
# for i in range(val_size):
#     for j in range(i+1,val_size):
#         if arr[i][0]>arr[j][0] and arr[i][1]>arr[j][1]:
#             ans[j]+=1
#         elif arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]:
#             ans[i]+=1
# for i in range(val_size):print(ans[i],end=' ')

# #4949
# while True:
#     s=input()
#     if len(s)==1 and s=='.':break
#     last=[]
#     chk=True
#     for i in range(len(s)):
#         if s[i]=='[' or s[i]=='(':
#             last.append(s[i])
#         elif s[i]==']':
#             if len(last)>0 and last.pop()=='[':continue
#             chk=False
#             break
#         elif s[i]==')':
#             if len(last)>0 and last.pop()=='(':continue
#             chk=False
#             break
#     if len(last)==0 and chk==True:print('yes')
#     else:print('no')

# #4153
# while True:
#     a=list(map(int,input().split()))
#     if sum(a)==0:break
#     a.sort()
#     if a[0]**2+a[1]**2==a[2]**2:print('right')
#     else:print('wrong')

# #2869
# import math
# a,b,v=map(int,input().split())
# v-=a
# print(math.ceil(v/(a-b))+1)

# #2839
# n=int(input())
# b3=0
# b5=int(n/5)
# def returnWeigh(b5,b3):
#     return b5*5+b3*3
# cnt=returnWeigh(b5,b3)
# while cnt!=n:
#     if b5<0:break
#     while cnt<n:
#         b3+=1
#         cnt+=3
#     if cnt>n:
#         b5-=1
#         b3=0
#         cnt=returnWeigh(b5,b3)
# if b5>=0:print(b3+b5)
# else:print(-1)

# #2805
# val_tree,val_meter=map(int,input().split())
# inf_tree=list(map(int,input().split()))
# inf_tree.sort()
# st=0
# ed=max(inf_tree)
# while st<=ed:
#     sumM=0
#     md=int((st+ed)/2)
#     for i in range(val_tree):
#         tmp=inf_tree[i]-md
#         if tmp>0:sumM+=tmp
#     if sumM<val_meter:ed=md-1
#     else:st=md+1
# print(ed)

# #2275
# val_case=int(input())
# for tn in range(val_case):
#     k=int(input())
#     n=int(input())
#     inf=[[0 for j in range(n)] for i in range(k+1)]
#     for i in range(n):inf[0][i]=i+1
#     for i in range(k+1):inf[i][0]=1

#     for i in range(1,k+1):
#         sumV=1
#         for j in range(1,n):
#             sumV+=inf[i-1][j]
#             inf[i][j]=sumV
#     print(inf[k][n-1])

# #2292
# k=int(input())
# sumV=1
# addV=6
# cnt=1
# while sumV<k:
#     sumV+=addV*cnt
#     cnt+=1
# print(cnt)

# #2108
# val_size=int(input())
# db_num=[]
# db_cnt=[0]*val_size
# for i in range(val_size):db_num.append(int(input()))
# db_num.sort()
# cnt=1
# tmp=db_num[0]
# db_cnt[0]=1
# for i in range(1,val_size):
#     if tmp!=db_num[i]:
#         cnt=1
#         tmp=db_num[i]
#     else:
#         cnt+=1
#     db_cnt[i]=cnt
# cnt=-1
# tmp=max(db_cnt)
# for i in range(val_size):
#     if db_cnt[i]==tmp:
#         if cnt==-1:cnt=i
#         else:
#             cnt=i
#             break

# print(round(sum(db_num)/val_size))
# print(db_num[int(val_size/2)])
# print(db_num[cnt])
# print(db_num[val_size-1]-db_num[0])

# #1966
# def pop_and_push(arr):
#     tmp=arr.pop(0)
#     arr.append(tmp)

# val_case=int(input())
# for i in range(val_case):
#     val_size,val_idx=map(int,input().split())
#     db_score=list(map(int,input().split()))
    
#     db_idx=list(range(val_size))
#     sv_idx=db_score[val_idx]
#     sv_max=max(db_score)
#     cnt=1

#     while sv_max>sv_idx:
#         while db_score[0]!=sv_max:
#             pop_and_push(db_score)
#             pop_and_push(db_idx)
#         db_score.pop(0)
#         db_idx.pop(0)
#         cnt+=1
#         sv_max=max(db_score)
#     for i in range(len(db_score)):
#         if db_idx[i]!=val_idx:
#             if db_score[i]==sv_idx:cnt+=1
#         else:break
#     print(cnt)

# #2231
# import sys
# val_find=int(input())
# val_len=len(str(val_find))
# def find_val(val):
#     sumC=val
#     sumV=0
#     while len(str(sumC))>1:
#         sumV+=sumC%10
#         sumC=int(sumC/10)
#     return sumV+sumC+val
# cnt=0
# while True:
#     st=find_val(cnt)
#     ed=st+18
#     if val_find<st:break
#     if val_find>=st or val_find<=ed:
#         for i in range(cnt,cnt+10):
#             if find_val(i)==val_find:
#                 print(i)
#                 sys.exit(0)
#     cnt+=10
# print(0)

# #1929
# n,k=map(int,input().split())
# a=[True]*(k+1)
# p=[2]
# a[1]=False
# for i in range(4,k,2):a[i]=False
# cnt=3
# while cnt<=k:
#     if a[cnt]==False:
#         cnt+=2
#         continue
#     p.append(cnt)
#     for i in range(cnt*2,k+1,cnt):a[i]=False
#     cnt+=2
# cnt=0
# while p[cnt]<n:cnt+=1
# for i in range(cnt,len(p)):print(p[i])

# n,k=map(int,input().split())
# cnt=3
# arr=[2]
# ans_cnt=0
# def find_min(arr,st,ed):
#     global ans_cnt
#     if st>ed:return
#     if st%2==0:st+=1
#     while st<=ed:
#         chk=False
#         for i in range(1,len(arr)):
#             if arr[i]*2>st:break
#             if st%arr[i]==0:
#                 chk=True
#                 break
#         if chk==False:arr.append(st)
#         st+=2
#     if ans_cnt==0:ans_cnt=len(arr)
# find_min(arr,3,n)
# find_min(arr,n,k)
# for i in range(ans_cnt,len(arr)):print(arr[i])

# #1874
# n=int(input())
# ans=[]
# stk=[]
# inf=[]
# for i in range(n):inf.append(int(input()))
# cnt_inf=0
# cnt_stk=0
# while cnt_stk<n:
#     cnt_stk+=1
#     stk.append(cnt_stk)
#     ans.append('+')
#     if cnt_stk==inf[cnt_inf]:
#         while len(stk)>0 and stk[len(stk)-1]==inf[cnt_inf]:
#             cnt_inf+=1
#             ans.append('-')
#             stk.pop()
# if cnt_inf==n:
#     for i in range(len(ans)):print(ans[i])
# else:print('NO')  

# #1654
# k,n=map(int,input().split())
# arr=[]
# chk=[]
# for i in range(k):arr.append(int(input()))
# arr.sort()
# st=1
# ed=arr[k-1]
# while st<=ed:
#     md=int((st+ed)/2)
#     cnt=0
#     for i in range(k):
#         cnt+=int(arr[i]/md)
#     if cnt<n:ed=md-1
#     else:st=md+1
# print(ed)
    
# #1436
# order=int(input())
# def chk_666(num):
#     cnt=0
#     while num>0:
#         if num%10==6:cnt+=1
#         else:cnt=0
#         if cnt>=3:return True
#         num=int(num/10)
#     return False
# num=666
# while order>0:
#     if chk_666(num)==True:
#         order-=1
#         if order==0:break
#     num+=1
# print(num)

# #11866
# n,k=map(int,input().split())
# a=[]
# for i in range(1,n+1):a.append(i) 
# idx=0
# print('<',end='')
# while n>1:
#     idx+=(k-1)
#     while idx>=n:idx-=n
#     print(a[idx],end=', ')
#     del a[idx]
#     n-=1
# print(str(a[0])+'>')

# #11650
# n=int(input())
# k=[]
# for i in range(n):
#     a,b=map(int,input().split())
#     k.append((a,b))
# k = list(set(k))
# k.sort()
# for i in range(n):print(str(k[i][0])+' '+str(k[i][1]))


# #11050
# n,k=map(int,input().split())
# def cal_pac(num):
#     if num==0:return 1
#     tmp = 1
#     while num>0:
#         tmp *= num
#         num-=1
#     return tmp
# if n>=k and k>=0:print(int(cal_pac(n)/(cal_pac(k)*cal_pac(n-k))))
# else:print('0')

# #10814
# k=[0]*201
# n=int(input())
# l=[]
# for i in range(n):
#     tmp,name=input().split()
#     age=int(tmp)
#     order=k[age]
#     k[age]+=1
#     l.append((age,name,order))
# l.sort(key = lambda x:x[0])
# cnt=0
# while cnt<n:
#     st=cnt
#     ed=cnt
#     while ed+1<n and l[st][0]==l[ed+1][0]:ed+=1
#     if st==ed:cnt+=1
#     else:cnt=ed+1
#     l[st:ed].sort(key = lambda x:x[2])
# for i in range(n):
#     print(str(l[i][0])+' '+l[i][1])

# #10250
# c=int(input())
# for c0 in range(c,0,-1):
#     h,w,n=map(int,input().split())
#     x=1
#     y=n
#     while y>h:
#         y-=h
#         x+=1
#     print(y*100+x)
    
# #9012
# n=int(input())
# for m in range(n):
#     a=input()
#     c=0
#     for i in range(len(a)):
#         if a[i]=='(':c+=1
#         else:c-=1
#         if c<0:
#             print("NO")
#             break
#         if i==len(a)-1:
#             if c==0:print("YES")
#             else:print("NO")

# #2789
# import sys
# n=int(input())
# a=list(map(int,input().split()))
# b=0
# for i in range(n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             t=a[i]+a[j]+a[k]
#             if t<=b:continue
#             if t>=m:
#                 if t>m:continue
#                 else:
#                     print(t)
#                     sys.exit()              
#             b=t
# print(b)
            
# #2751
# n=int(input())
# a=[]
# for i in range(n):a.append(int(input()))

# def sort_quick(a,st,ed):
#     if st>=ed:return
#     if ed-st<=100:
#         sort_insert(a,st,ed)
#         return
#     lt=st+1
#     rt=ed
#     while lt<rt:
#         while a[lt]<=a[st]:lt+=1
#         while a[rt]>=a[st]:rt-=1
#         if lt<rt:a[lt],a[rt]=a[rt],a[lt]
#     a[st],a[rt]=a[rt],a[st]
#     sort_quick(a,st,rt-1)
#     sort_quick(a,rt+1,ed)

# def sort_insert(a, st, ed):
#     for i in range(st, ed+1):
#         for j in range(i,st,-1):
#             if a[j]<a[j-1]:a[j],a[j-1]=a[j-1],a[j]
#             else:break

# sort_quick(a,0,n-1)
# for i in range(n):print(a[i])

# #2609
# a,b=map(int,input().split())
# def GCF(a,b):
#     while a>0 and b>0:
#         if a>b:a%=b
#         else:b%=a
#     a+=b
#     return a
# k=GCF(a,b)
# print(k)
# print(int(a*b/k))

# #1978
# n=int(input())
# a=[]
# for i in range(1,n+1):a.append(i)
# lim=n
# while lim>1:
#     a.pop(0)
#     lim-=1
#     tmp=a.pop(0)
#     a.append(tmp)
# print(a[0])  

#1920
# n=int(input())
# a=sorted(list(map(int,input().split())))
# k=int(input())
# b=list(map(int,input().split()))
# for i in range(k):
#     st=0
#     ed=n-1
#     while st<=ed:
#         md=int((st+ed)/2)
#         if a[md]==b[i]:break
#         if a[md]<b[i]:st=md+1
#         else:ed=md-1
#     if a[md]==b[i]:print('1')
#     else:print('0') 
    

# #1259
# while True:
#     k=input()
#     if int(k)==0:break
#     r=k[::-1]
#     if int(k)==int(r):print("yes")
#     else:print("no")

# #1181
# n=int(input())
# k=[]
# for i in range(n):k.append(input())
# k = list(set(k))
# k=sorted(k)
# k.sort(key=len)
# for i in range(len(k)):print(k[i])

# #1085
# x,y,w,h=map(int,input().split())
# k=[]
# k.append(x-0)
# k.append(w-x)
# k.append(y-0)
# k.append(h-y)
# print(min(k))

# #1018
# map_col, map_row = map(int, input().split())
# map_info=[]
# for i in range(map_col):
#     map_info.append(input())

# val_max = 65
# chk_1 = "WBWBWBWB"
# chk_2 = "BWBWBWBW"

# def chk_same(str_F, str_L, rL, cL, mapI):
#     val_sW = 0
#     val_sB = 0
#     for i in range(8):
#         for j in range(8):
#             if i%2==0:
#                 if str_F[j]!=mapI[rL+i][cL+j]:val_sW+=1
#                 if str_L[j]!=mapI[rL+i][cL+j]:val_sB+=1
#             else:
#                 if str_L[j]!=mapI[rL+i][cL+j]:val_sW+=1
#                 if str_F[j]!=mapI[rL+i][cL+j]:val_sB+=1
#     if val_sB<val_sW:val_sW=val_sB
#     return val_sW

# for i in range(0, map_col - 7):
#     for j in range(0, map_row - 7):
#         val_tmp=chk_same(chk_1,chk_2,i,j,map_info)
#         if val_max>val_tmp:val_max=val_tmp

# print(val_max)