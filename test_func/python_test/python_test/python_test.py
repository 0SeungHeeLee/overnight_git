import sys
sys.setrecursionlimit(100000)
unit_M,build_hp,build_gn=map(int,input().split())
unit_E=0
turn_min=999999

def turn_attackE(mine,enemy,hp):
    return mine-enemy

def turn_generate(enemy,hp,generate):
    if hp>0:return enemy+generate
    else:return enemy

def chk_win(enemy,hp):
    if enemy==0 and hp==0:return True
    else:return False

def chk_lose(mine):
    if mine<=0:return True
    else:return False

def chk_battle(mine,enemy):
    while mine>0 and enemy>0:
        mine-=enemy
        enemy-=mine
    if mine>enemy:return True
    else:return False

def chk_loop(mine,hp,generate):
    if hp-mine>0 and mine<=generate:return True
    else:return False

def set_attack(mine,enemy,hp):
    if hp<=0:
        tBuild=0
        tEnemy=mine
    elif mine>=hp:
        tBuild=hp
        tEnemy=mine-hp
    elif mine>=enemy:
        tBuild=mine-enemy
        tEnemy=enemy
    else:
        tBuild=mine
        tEnemy=0
    return tBuild,tEnemy 
def set_dirVal(tB,tE):
    if tB>=tE:return -1,1
    else:return 1,-1
def simulator(mine,enemy,hp,turn):
    global build_gn
    global turn_min

    if chk_win(enemy,hp):
        if turn_min>turn:turn_min=turn
        return
    if turn>=turn_min:return

    mine=turn_attackE(mine,enemy,hp)
    if chk_lose(mine):return
    if chk_loop(mine,hp,build_gn):return
    enemy=turn_generate(enemy,hp,build_gn)
    turn+=1

    attack_toBuild,attack_toEnemy=set_attack(mine,enemy,hp)
    v_tB,v_tE=set_dirVal(attack_toBuild,attack_toEnemy)
    while attack_toEnemy>=0 and attack_toBuild>=0:
        if chk_battle(mine,enemy)==True:simulator(mine,enemy-attack_toEnemy,hp-attack_toBuild,turn)
        attack_toBuild+=v_tB
        attack_toEnemy+=v_tE
def chk_shorter(mine,enemy,hp,turn):
    global build_gn
    global turn_min

    if hp-mine<=0:return mine,enemy,hp,turn
    if build_gn>=mine:
        print(-1)
        sys.exit()
    dmg=mine-build_gn
    while hp>mine:
        hp-=dmg
        turn+=1
    return mine,enemy,hp,turn

mine,enemy,hp,turn=chk_shorter(unit_M,unit_E,build_hp-unit_M,1)
simulator(mine,enemy,hp,turn)
if turn_min==999999:print(-1)
else:print(turn_min)