map_col = int(input())
map_row = int(input())
map_info = []

for i in range(0, map_col):
    tmp_str = input()
    map_info.append(list(tmp_str))

print(map_info)

#알파벳 개수: 26, A 아스키코드: 65 ord()
alp_max = 26
alp_decA = 65
alp_chk = []
for i in range(0, alp_max):
    alp_chk.append(int(0))
#alp_chk[ord(map_info[0][0])] = 1

dicConst = {'mC' : map_col, 'mR' : map_row, 'aMax' : alp_max, 'aDec' : alp_decA}

def find_Ans(mInfo, aChk, minM, cnt, locC, locR, dic):
    if locC < 0 or locC >= mC:
        return
    if locR < 0 or locR >= mR:
        return
    key = ord(alp_chk[locX][locY])
    if aChk[key-dicConst['aDec']] == 1:
       return
    

print(find_Ans(map_info, alp_chk, map_col*map_row+1, 0, 0, 0, dicConst))