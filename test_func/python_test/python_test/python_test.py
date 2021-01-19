#17142
from itertools import combinations
map_size,virus_active=map(int,input().split())
map_inf=[]
virus_inf=[]
for i in range(map_size):
    map_inf.append([])
    map_inf[i]=list(map(int,input().split()))
for i in range(map_size):
    for j in range(map_size):
        if map_inf[i][j]==2:
            virus_inf.append([i,j])

db_dir=[[0,1],[0,-1],[1,0],[-1,0]]
virus_idx=[]
for i in combinations(virus_inf,virus_active):virus_idx.append(i)
time_min=map_size*map_size

def task_find(map,size):
    global time_min
    global db_dir

    ed=0
    stair=[]
    queue=[]
    check=[[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            if map[i][j]==3:
                queue.append([])
                queue[len(queue)-1].append(i)
                queue[len(queue)-1].append(j)
                check[i][j]=1
                stair.append(0)
    while len(queue)>ed:
        for i in range(4):
            mi=queue[ed][0]+db_dir[i][0]
            mj=queue[ed][1]+db_dir[i][1]
            if mi<0 or mj<0 or mi>=size or mj>=size:continue
            if map[mi][mj]==1:continue
            if check[mi][mj]>0:continue
            queue.append([])
            queue[len(queue)-1].append(mi)
            queue[len(queue)-1].append(mj)
            check[mi][mj]=1
            stair.append(stair[ed]+1)
        ed+=1
    for i in range(size):
        for j in range(size):
            if map[i][j]!=1 and check[i][j]==0:return
    cnt=ed-1
    while cnt>=0:
        if map[queue[cnt][0]][queue[cnt][1]]!=2:break
        cnt-=1
    tmp_min=stair[cnt]
    if tmp_min<time_min:time_min=tmp_min

for i in range(len(virus_idx)):
    for j in range(len(virus_idx[0])):
        map_inf[virus_idx[i][j][0]][virus_idx[i][j][1]]=3
    task_find(map_inf,map_size)
    for j in range(len(virus_idx[0])):
        map_inf[virus_idx[i][j][0]][virus_idx[i][j][1]]=2

if time_min<map_size*map_size:print(time_min)
else:print(-1)