#1572
import sys
num_len,time_val=map(int,sys.stdin.readline().split())
num_db=[int(sys.stdin.readline()) for _ in range(num_len)]

time_divid2=int((time_val+1)/2)
time_sum=0
cal_val=1
num_mx=max(num_db)

class NODE:
    def __init__(self,st,ed):
        self.st=st
        self.ed=ed
        self.val=0
        self.lt=None
        self.rt=None
class LINKED_LIST:
    def __init__(self):
        global num_mx
        self.loc_front=NODE(1,num_mx)
    def setSegment(self,nod):
        if nod.st==nod.ed:return
        md=int((nod.st+nod.ed)/2)
        nod.lt=NODE(nod.st,md)
        self.setSegment(nod.lt)
        nod.rt=NODE(md+1,nod.ed)
        self.setSegment(nod.rt)
    def changeSegment(self,nod,findVal):
        global cal_val
        nod.val+=cal_val
        if nod.st==nod.ed:return

        if nod.lt.st<=findVal and findVal<=nod.lt.ed:self.changeSegment(nod.lt,findVal)
        else:self.changeSegment(nod.rt,findVal)
    def findSegment(self,nod,stk):
        global time_divid2
        global time_sum

        if nod.st==nod.ed:
            time_sum+=nod.st
            return
        
        if nod.lt.val+stk>=time_divid2:self.findSegment(nod.lt,stk)
        else:self.findSegment(nod.rt,stk+nod.lt.val)

seg_inf=LINKED_LIST()
seg_inf.setSegment(seg_inf.loc_front)
tL=time_val-1
for i in range(tL):seg_inf.changeSegment(seg_inf.loc_front,num_db[i])
for i in range(tL,num_len):
    cal_val=1
    seg_inf.changeSegment(seg_inf.loc_front,num_db[i])
    seg_inf.findSegment(seg_inf.loc_front,0)
    cal_val=-1
    seg_inf.changeSegment(seg_inf.loc_front,num_db[i-tL])

print(time_sum)


# #1306
# import sys
# road_len,sight_val=map(int,sys.stdin.readline().split())
# road_db=list(map(int,sys.stdin.readline().split()))

# road_db.insert(0,0)
# sight_lim=road_len-sight_val+2
# seg_len=1
# while seg_len<road_len:seg_len*=2
# seg_len*=2
# seg_len+=1
# seg_maxDB=[0]*seg_len
# seg_secDB=[[0,0] for _ in range(seg_len)]
# def segment_set(loc,st,ed):
#     global road_db
#     global seg_maxDB
#     global seg_secDB

#     seg_maxDB[loc]=max(road_db[st:ed+1])
#     seg_secDB[loc][0]=st
#     seg_secDB[loc][1]=ed

#     if st>=ed:return

#     md=int((st+ed)/2)
#     segment_set(loc*2,st,md)
#     segment_set(loc*2+1,md+1,ed)
# segment_set(1,1,road_len)

# seg_maxVal=0
# def segment_setMax(x):
#     global seg_maxVal
#     if seg_maxVal<x:seg_maxVal=x

# def segment_find(loc,st,ed):
#     global seg_maxDB
#     global seg_secDB

#     if st==seg_secDB[loc][0] and ed==seg_secDB[loc][1]:
#         segment_setMax(seg_maxDB[loc])
#         return

#     st_lt=seg_secDB[loc*2][0]       #1
#     ed_lt=seg_secDB[loc*2][1]       #3
#     st_rt=seg_secDB[loc*2+1][0]     #4

#     if st_lt<=st and st<st_rt:
#         if ed<=ed_lt:segment_find(loc*2,st,ed)
#         else:
#             segment_find(loc*2,st,ed_lt)
#             segment_find(loc*2+1,st_rt,ed)
#     else:
#         segment_find(loc*2+1,st,ed)

# for x in range(sight_val,sight_lim):
#     seg_maxVal=0
#     segment_find(1,x-sight_val+1,x+sight_val-1)
#     print(seg_maxVal,end=' ')

# #1321
# import sys
# unit_len=int(input())
# unit_db=list(map(int,sys.stdin.readline().split()))
# unit_db.insert(0,0)
# task_db=[]
# seg_len=1
# while seg_len<unit_len:seg_len*=2
# seg_len*=2
# seg_len+=1
# sag_infDB=[0]*seg_len
# sag_secDB=[[0,0] for _ in range(seg_len)]
# def sagment_set(loc,st,ed):
#     global unit_db
#     global sag_infDB
#     global sag_secDB

#     sag_infDB[loc]=sum(unit_db[st:ed+1])
#     sag_secDB[loc][0]=st
#     sag_secDB[loc][1]=ed

#     if st>=ed:return

#     md=int((st+ed)/2)
#     sagment_set(loc*2,st,md)
#     sagment_set(loc*2+1,md+1,ed)
# sagment_set(1,1,unit_len)

# def sagment_change(loc):
#     global sag_infDB
#     global sag_secDB
#     global task_db

#     sag_infDB[loc]+=task_db[2]
#     if sag_secDB[loc][0]==sag_secDB[loc][1]:return
#     if sag_secDB[loc*2][0]<=task_db[1] and task_db[1]<=sag_secDB[loc*2][1]:sagment_change(loc*2)
#     else:sagment_change(loc*2+1)
# def sagment_find(loc,stk):
#     global sag_infDB
#     global sag_secDB
#     global task_db
    
#     if sag_secDB[loc][0]==sag_secDB[loc][1]:
#         print(sag_secDB[loc][0])
#         return

#     if stk+sag_infDB[loc*2]>=task_db[1]:sagment_find(loc*2,stk)
#     else:sagment_find(loc*2+1,stk+sag_infDB[loc*2])


# task_len=int(input())
# for _ in range(task_len):
#     task_db=list(map(int,sys.stdin.readline().split()))
#     if len(task_db)==3:
#         unit_db[task_db[1]]+=task_db[2]
#         sagment_change(1)
#     else:sagment_find(1,0)
