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