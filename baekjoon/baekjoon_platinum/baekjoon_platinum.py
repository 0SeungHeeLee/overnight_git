#1321
import sys
unit_len=int(input())
unit_db=list(map(int,sys.stdin.readline().split()))
unit_db.insert(0,0)
task_db=[]
seg_len=1
while seg_len<unit_len:seg_len*=2
seg_len*=2
seg_len+=1
sag_infDB=[0]*seg_len
sag_secDB=[[0,0] for _ in range(seg_len)]
def sagment_set(loc,st,ed):
    global unit_db
    global sag_infDB
    global sag_secDB

    sag_infDB[loc]=sum(unit_db[st:ed+1])
    sag_secDB[loc][0]=st
    sag_secDB[loc][1]=ed

    if st>=ed:return

    md=int((st+ed)/2)
    sagment_set(loc*2,st,md)
    sagment_set(loc*2+1,md+1,ed)
sagment_set(1,1,unit_len)

def sagment_change(loc):
    global sag_infDB
    global sag_secDB
    global task_db

    sag_infDB[loc]+=task_db[2]
    if sag_secDB[loc][0]==sag_secDB[loc][1]:return
    if sag_secDB[loc*2][0]<=task_db[1] and task_db[1]<=sag_secDB[loc*2][1]:sagment_change(loc*2)
    else:sagment_change(loc*2+1)
def sagment_find(loc,stk):
    global sag_infDB
    global sag_secDB
    global task_db
    
    if sag_secDB[loc][0]==sag_secDB[loc][1]:
        print(sag_secDB[loc][0])
        return

    if stk+sag_infDB[loc*2]>=task_db[1]:sagment_find(loc*2,stk)
    else:sagment_find(loc*2+1,stk+sag_infDB[loc*2])


task_len=int(input())
for _ in range(task_len):
    task_db=list(map(int,sys.stdin.readline().split()))
    if len(task_db)==3:
        unit_db[task_db[1]]+=task_db[2]
        sagment_change(1)
    else:sagment_find(1,0)
