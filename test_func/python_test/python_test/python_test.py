#1941
import copy
map_ver=[[0 for hor in range(4)] for ver in range(10)]
map_hor=[[0 for hor in range(10)] for ver in range(4)]
blk_dir=[[0,0],[0,0],[0,1],[1,0]]
val_score=0

def set_blkInf(cs,x,y,blk):
    global blk_dir

    blk.append([])
    blk[0].append(x)
    blk[0].append(y)
    blk.append([])
    blk[1].append(x+blk_dir[cs][1])
    blk[1].append(y+blk_dir[cs][0])
def cal_sumHor(x):
    global map_hor
    tmp=0
    for i in range(4):tmp+=map_hor[i][x]
    return tmp
def cal_blk():
    global map_ver
    global map_hor
    cnt_blk=0

    for i in range(6,10):
        for j in range(4):
            if map_ver[i][j]>0:cnt_blk+=1
            if map_hor[j][i]>0:cnt_blk+=1
    
    return cnt_blk
        
def chk_outRange():
    global map_ver
    global map_hor

    chkV=[sum(map_ver[5]),sum(map_ver[4])]
    chkH=[cal_sumHor(5),cal_sumHor(4)]
    if chkV[1]>0:cntV=2
    elif chkV[0]>0:cntV=1
    else:cntV=0
    if chkH[1]>0:cntH=2
    elif chkH[0]>0:cntH=1
    else:cntH=0

    if cntV>0:
        for i in range(9-cntV,9-cntV-6,-1):
            for j in range(4):map_ver[i+cntV][j]=map_ver[i][j]
    if cntH>0:
        for i in range(9-cntH,9-cntH-6,-1):
            for j in range(4):map_hor[j][i+cntH]=map_hor[j][i]

def chk_getScore(x):
    global map_ver
    global map_hor
    global val_score
    
    while True:
        chk_get=False
        for i in range(9,5,-1):
            for j in range(4):
                if map_ver[i][j]==0:break
                if j==3:
                    val_score+=1
                    for k in range(4):map_ver[i][k]=0
                    chk_get=True              
        if chk_get==False:break

        for i in range(8,3,-1):
            c2_chk=[-1]*4
            for j in range(4):
                if map_ver[i][j]==0:continue
                if map_ver[i][j]==2:c2_chk[j]=j
                else:
                    lY=i
                    while lY+1<10 and map_ver[lY+1][j]==0:
                        map_ver[lY+1][j]=map_ver[lY][j]
                        map_ver[lY][j]=0
                        lY+=1
            if sum(c2_chk)==-4:continue
            c2_chk.remove(-1)
            lY=i
            chk_crash=True
            while chk_crash:
                if lY>=9:break
                for j in c2_chk: 
                    if map_ver[lY+1][j]>0:
                        chk_crash=False
                        break
                if chk_crash:
                    for j in c2_chk: 
                        map_ver[lY+1][j]=map_ver[lY][j]
                        map_ver[lY][j]=0
                    lY+=1

    while True:
        chk_get=False
        for i in range(9,5,-1):
            for j in range(4):
                if map_hor[j][i]==0:break
                if j==3:
                    val_score+=1
                    for k in range(4):map_hor[k][i]=0
                    chk_get=True              
        if chk_get==False:break

        for i in range(8,3,-1):
            c3_chk=[-1]*4
            for j in range(4):
                if map_hor[j][i]==0:continue
                if map_hor[j][i]==3:c3_chk[j]=j
                else:
                    lX=i
                    while lX+1<10 and map_hor[j][lX+1]==0:
                        map_hor[j][lX+1]=map_hor[j][lX]
                        map_hor[j][lX]=0
                        lX+=1
            if sum(c3_chk)==-4:continue
            c3_chk.remove(-1)
            lX=i
            chk_crash=True
            while chk_crash:
                if lX>=9:break
                for j in c3_chk: 
                    if map_hor[j][lX+1]>0:
                        chk_crash=False
                        break
                if chk_crash:
                    for j in c3_chk: 
                        map_hor[j][lX+1]=map_hor[j][lX]
                        map_hor[j][lX]=0
                    lX+=1

def act_blkDrop(blkV,blkH,blkC):
    global map_ver
    global map_hor

    while blkV[1][1]<9 and map_ver[blkV[0][1]+1][blkV[0][0]]==0 and map_ver[blkV[1][1]+1][blkV[1][0]]==0:
        blkV[0][1]+=1
        blkV[1][1]+=1
    while blkH[1][0]<9 and map_hor[blkH[0][1]][blkH[0][0]+1]==0 and map_hor[blkH[1][1]][blkH[1][0]+1]==0:
        blkH[0][0]+=1
        blkH[1][0]+=1
    map_ver[blkV[0][1]][blkV[0][0]]=blkC
    map_ver[blkV[1][1]][blkV[1][0]]=blkC
    map_hor[blkH[0][1]][blkH[0][0]]=blkC
    map_hor[blkH[1][1]][blkH[1][0]]=blkC
    
def test_printDB():
    global map_ver
    global map_hor
    for i in range(4):
        print(map_hor[i])
    for i in range(4,10):
        print(map_ver[i])
    print('-------------------------------------------')


num_block=int(input())
for i in range(num_block):
    blk_case,blk_locY,blk_locX=map(int,input().split())
    blk_infV=[]
    set_blkInf(blk_case,blk_locX,blk_locY,blk_infV)
    blk_infH=copy.deepcopy(blk_infV)
    #print(blk_infV)

    act_blkDrop(blk_infV,blk_infH,blk_case)
    chk_getScore(i)
    chk_outRange()
    #test_printDB()

print(val_score)
print(cal_blk())