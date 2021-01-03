#include <stdio.h>
#include <stdlib.h>

#define MAX_VALUE 1234567
#define MX 10000

typedef struct UNIT {
	int mine;
	int enemy;
}uint;
typedef struct LOW_VALUE {
	uint marine;
	int build;
}lval;

typedef const int cint;

lval low_values[MX];
int low_turn;

void task_find(int vTurn, uint vMarine, int vBuild, cint sTrain);

int main()
{
	uint value_marine;
	int size_train;
	int value_build;
	int value_turn;
	int low_marine;
	int low_build;

	scanf("%d %d %d", &value_marine.mine, &value_build, &size_train);
	value_marine.enemy = value_turn = 0;
	low_marine = value_marine.mine;
	low_build = value_build;
	low_turn = MAX_VALUE;

	if (value_build - value_marine.mine < 0) {
		printf("1");
		return 0;
	}
	task_find(1, value_marine, value_build - value_marine.mine, size_train);

	if (low_turn == MAX_VALUE) printf("-1");
	else printf("%d", low_turn);


	return 0;
}

void task_find(int vTurn, uint vMarine, int vBuild, cint sTrain)
{
	int tmp_cnt;

	if (vTurn > low_turn) return;

	//상대턴
	vMarine.mine -= vMarine.enemy;
	if (vMarine.mine <= 0) return;
	if (vBuild > 0) vMarine.enemy += sTrain;
	vTurn++;

	//경우의 수 축소
	if (vBuild - vMarine.mine < 0) tmp_cnt = vMarine.mine - vBuild;
	else tmp_cnt = 0;

	//내 턴
	for (int i = tmp_cnt; i <= vMarine.mine; i++) {
		vBuild -= (vMarine.mine - i);
		vMarine.enemy -= i;

		if (vBuild <= 0 && vMarine.enemy <= 0) {
			if (vTurn < low_turn) low_turn = vTurn;
			return;
		}

		task_find(vTurn, vMarine, vBuild, sTrain);

		vMarine.enemy += i;
		vBuild += (vMarine.mine - i);
	}
}