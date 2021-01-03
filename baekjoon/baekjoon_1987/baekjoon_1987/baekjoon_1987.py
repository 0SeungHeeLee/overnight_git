import sys
sys.setrecursionlimit(100000)

map_col = int(input())
map_row = int(input())
map_info = []
map_chk = [[0 for col in range(20)] for row in range(20)]

for i in range(0, map_col):
    tmp_str = input()
    map_info.append(list(tmp_str))

print(map_info)

#알파벳 개수: 26, A 아스키코드: 65 ord()
alp_decA = 65
alp_chk = []
for i in range(0, 26):
    alp_chk.append(int(0))
dicConst = {'mC' : map_col, 'mR' : map_row, 'aDec' : alp_decA}
g_min = 0

def find_Ans(mInfo, aChk, mChk, locC, locR, dic):
    global g_min
    if locC < 0 or locC >= dic['mC']:
        return 0
    if locR < 0 or locR >= dic['mR']:
        return 0
    key = ord(mInfo[locC][locR]) - dic['aDec']
    if aChk[key] == 1 or mChk[locC][locR] == 1:
       return 0

    aChk[key] = 1
    mChk[locC][locR] = 1
    end_chk = 0

    tChk = aChk

    end_chk += find_Ans(mInfo, tChk, mChk, locC + 1, locR, dic)
    end_chk += find_Ans(mInfo, tChk, mChk, locC - 1, locR, dic)
    end_chk += find_Ans(mInfo, tChk, mChk, locC, locR + 1, dic)
    end_chk += find_Ans(mInfo, tChk, mChk, locC, locR - 1, dic)

    if end_chk == 0:
        alp_cnt = 0
        for i in range(0, 26):
            if aChk[i] == 1:
                print(chr(i+65), end='')
                alp_cnt += 1

        print()
        for i in range(0, 20):
            for j in range(0, 20):
                print(mChk[i][j], end='')
            print()
        print()
        if alp_cnt > g_min:
            g_min = alp_cnt
    
    return 1

tmp = find_Ans(map_info, alp_chk, map_chk, 0, 0, dicConst)
print(g_min)