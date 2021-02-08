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
            print(nod.st)
            time_sum+=nod.st
            return
        
        if nod.lt.val+stk>=time_divid2:self.findSegment(nod.lt,stk)
        else:self.findSegment(nod.rt,stk+nod.lt.val)
    def chkSegment(self,nod):
        tmp=str(nod.st)+' '+str(nod.ed)+": "+str(nod.val)
        print(tmp,end=' / ')
        if nod.st==nod.ed:return
        self.chkSegment(nod.lt)
        self.chkSegment(nod.rt)

seg_inf=LINKED_LIST()
seg_inf.setSegment(seg_inf.loc_front)
tL=time_val-1
for i in range(tL):seg_inf.changeSegment(seg_inf.loc_front,num_db[i])
for i in range(tL,num_len):
    cal_val=1
    seg_inf.changeSegment(seg_inf.loc_front,num_db[i])
    seg_inf.chkSegment(seg_inf.loc_front)
    seg_inf.findSegment(seg_inf.loc_front,0)
    cal_val=-1
    seg_inf.changeSegment(seg_inf.loc_front,num_db[i-tL])

print(time_sum)