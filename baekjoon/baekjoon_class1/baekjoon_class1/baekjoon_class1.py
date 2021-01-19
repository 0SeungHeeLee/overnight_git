n=int(input())
a=[]
for i in range(1,n+1):a.append(i)
lim=n
while lim>1:
    a.pop(0)
    lim-=1
    tmp=a.pop(0)
    a.append(tmp)
print(a[1])

##10998
#a,b=map(int,input().split())
#print(a*b)
 
##10809
#a=input()
#b=[-1]*26
#for i in range(len(a)):
#    if b[ord(a[i])-97]==-1:b[ord(a[i])-97]=i
#for i in range(26): print(b[i],end=' ')

##10172
#print("|\\_/|")
#print("|q p|   /}")
#print("( 0 )\"\"\"\\")
#print("|\"^\"`    |")
#print("||_/=\\\\__|")

##3052
#a=[]
#b=[]
#for i in range(10):a.append(int(input()))
#for i in range(10):
#    k=a[i]%42
#    l=False
#    for j in range(len(b)):
#        if b[j]==k:l=True
#    if l==False:
#        b.append(k)
#print(len(b))

##2908
#a,b=map(str,input().split())
#a=int(a[::-1])
#b=int(b[::-1])
#if a>b:print(a)
#else:print(b)

##2884
#a,b=map(int,input().split())
#b-=45
#if b<0:
#    b+=60
#    a-=1
#if a<0:
#    a+=24
#print(str(a)+' '+str(b))

##2753
#a=int(input())
#b=False
#if a%4==0 and a%100!=0:b=True
#if a%400==0:b=True
#if b==True:print('1')
#else:print('0')

##2742
#a=int(input())
#for i in range(a,0,-1):print(i)

##2741
#a=int(input())
#for i in range(1,a+1):print(i)

##2577
#a=[0]*10
#b=[]
#for i in range(3):b.append(int(input()))
#s=b[0]*b[1]*b[2]
#while s>0:
#    a[s%10]+=1
#    s=int(s/10)
#for i in range(10):print(a[i])

##2475
#a=list(map(int,input().split()))
#for i in range(5):a[i]*=a[i]
#print(sum(a)%10)

##2439
#n=int(input())
#for i in range(1,n+1):
#    for j in range(n-i):print(' ',end='')
#    for j in range(i):print('*',end='')
#    print()

##1546
#n=int(input())
#a=list(map(float, input().split()))
#m=max(a)
#for i in range(len(a)):
#    a[i]=a[i]/m*100
#print(sum(a)/len(a))

##1157
#import sys
#a=[0]*26
#s=input()
#for i in range(len(s)):
#    k=ord(s[i])
#    if k>=97:a[k-97]+=1
#    else:a[k-65]+=1
#m=max(a)
#c=0
#for i in range(26):
#    if a[i]==m:c+=1
#    if c>=2:
#        print('?')
#        sys.exit()
#print(chr(65+a.index(max(a))))


##1152
#a=input()
#k=a.count(' ')+1
#if a[0]==' ':k-=1
#if a[len(a)-1]==' ':k-=1
#print(k)

##11720
#t=int(input())
#a=input()
#s=0
#for i in range(t):s+=int(a[i])
#print(s)

##11654
#a=input()
#print(ord(a))

##10952
#while True:
#    a,b=map(int,input().split())
#    if a==b and a==0:break
#    print(a+b)

##10951
#while True:
#    try:
#        a,b=map(int,input().split())
#        print(a+b)
#    except EOFError:
#        break

##10950
#n=int(input())
#for i in range(n):
#    a,b=map(int,input().split())
#    print(a+b)

##10869
#a,b=map(int,input().split())
#print(a+b)
#print(a-b)
#print(a*b)
#print(int(a/b))
#print(a%b)

##8958
#n=int(input())
#for i in range(n):
#    a=input()
#    b=0
#    c=0
#    for j in range(len(a)):
#        if a[j]=='O':
#            b+=1
#            c+=b
#        else:b=0
#    print(c)

##2920
#c=0
#a=list(map(int,input().split()))
#for i in range(0,8):
#    if a[i]!=i+1:break
#    if i==7:c=1
#for i in range(0,8):
#    if a[i]!=8-i:break
#    if i==7:c=2
#if c==1:print("ascending")
#elif c==2:print("descending")
#else:print("mixed")

##2739
#n=int(input())
#for i in range(1,10):
#    print(str(n)+" * "+str(i)+" = "+str(i*n))

##2675
#n=int(input())
#for i in range(0,n):
#    t,s=input().split()
#    for j in range(len(s)):
#        for k in range(int(t)):
#            print(s[j],end='')
#    print()


##2562
#a=[]
#for i in range(9):a.append(int(input()))
#print(max(a))
#print(a.index(max(a))+1)

##2438
#n=int(input())
#for i in range(1,n+1):
#    for j in range(0,i): print('*',end='')
#    print()

##1330
#a,b=map(int,input().split())
#if a-b>0:print('>')
#elif a-b<0:print('<')
#else:print("==")

##1008
#a,b=map(float,input().split())
#print(a/b)

##1001
#a,b=map(int,input().split())
#print(a-b)