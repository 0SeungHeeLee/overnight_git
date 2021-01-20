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