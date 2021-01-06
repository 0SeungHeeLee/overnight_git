#1978
n=int(input())
a=list(map(int,input().split()))
def isPrime(k):
    if k==1:return 0
    if k==2:return 1
    if k%2==0:return 0
    c=3
    while c<=int(k/2):
        if k%c==0:return 0
        c+=2
    return 1
s=0
for i in range(n):s+=isPrime(a[i])
print(s)

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