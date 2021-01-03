#include <stdio.h>
#include <stdlib.h>

#define EMPTY -1234567
#define SET_MAX -1
#define SET_MIN 1000000001

typedef struct PAIRS {
	int st;
	int ed;
}pir;
typedef struct AMOUNT {
	int min;
	int max;
	int st;	//범위 시작
	int ed;	//범위 끝
	int lt;	//자식노드 (좌)
	int rt;	//자식노드 (우)
	int bs;	//어미노드
}ant;
typedef const int cint;

void find_specialValue(int loc, int* dV, ant* dN);

void task_setNod(cint sV, cint sS, int* dV, ant* dN);
void task_findNod(int loc, int lt, int rt, int* low, int* high, ant* dN);

int main()
{
	int* data_val;		//번호
	pir* data_sec;		//구간
	ant* data_nod;		//세그먼트
	int size_val;
	int size_sec;
	pir tmp_ans;

	scanf("%d %d", &size_val, &size_sec);
	data_val = (int*)malloc(sizeof(int) * (size_val + 1));
	data_sec = (pir*)malloc(sizeof(pir) * (size_sec));
	data_nod = (ant*)malloc(sizeof(ant) * (size_val * 3));

	for (int i = 1; i <= size_val; i++)
		scanf("%d", &data_val[i]);
	for (int i = 0; i < size_sec; i++)
		scanf("%d %d", &data_sec[i].st, &data_sec[i].ed);

	task_setNod(size_val, size_sec, data_val, data_nod);
	for (int i = 0; i < size_sec; i++) {
		tmp_ans.st = SET_MIN;
		tmp_ans.ed = SET_MAX;
		task_findNod(1, data_sec[i].st, data_sec[i].ed, &tmp_ans.st, &tmp_ans.ed, data_nod);
		printf("%d %d\n", tmp_ans.st, tmp_ans.ed);
	}
}

void find_specialValue(int loc, int* dV, ant* dN)
{
	int value_min;
	int value_max;

	value_min = SET_MIN;
	value_max = SET_MAX;

	for (int i = dN[loc].st; i <= dN[loc].ed; i++) {
		if (dV[i] > value_max) value_max = dV[i];
		if (dV[i] < value_min) value_min = dV[i];
	}
	dN[loc].min = value_min;
	dN[loc].max = value_max;
}

void task_setNod(cint sV, cint sS, int* dV, ant* dN)
{
	int cnt_st = 1;
	int cnt_ed = 1;

	dN[cnt_st].bs = EMPTY;
	if (sV >= 2) {
		dN[cnt_st].lt = ++cnt_ed;
		dN[cnt_ed].st = 1;
		dN[cnt_ed].ed = sV / 2;
		dN[cnt_ed].bs = cnt_st;

		dN[cnt_st].rt = ++cnt_ed;
		dN[cnt_ed].st = sV / 2 + 1;
		dN[cnt_ed].ed = sV;
		dN[cnt_ed].bs = cnt_st;
	}
	else dN[cnt_st].lt = dN[cnt_st].rt = EMPTY;
	
	dN[cnt_st].st = 1;
	dN[cnt_st].ed = sV;
	find_specialValue(cnt_st, dV, dN);
	//min, max, st, ed, lt, rt, bs

	while (++cnt_st <= cnt_ed) {
		if (dN[cnt_st].st == dN[cnt_st].ed) {
			dN[cnt_st].lt =	dN[cnt_st].rt = EMPTY;
			dN[cnt_st].max = dN[cnt_st].min = dV[dN[cnt_st].st];
			continue;
		}

		find_specialValue(cnt_st, dV, dN);

		dN[cnt_st].lt = ++cnt_ed;
		dN[cnt_ed].st = dN[cnt_st].st;
		dN[cnt_ed].ed = (dN[cnt_st].st + dN[cnt_st].ed) / 2;
		dN[cnt_ed].bs = cnt_st;

		dN[cnt_st].rt = ++cnt_ed;
		dN[cnt_ed].st = (dN[cnt_st].st + dN[cnt_st].ed) / 2 + 1;
		dN[cnt_ed].ed = dN[cnt_st].ed;
		dN[cnt_ed].bs = cnt_st;
	}
}

void task_findNod(int loc, int lt, int rt, int* low, int* high, ant* dN)
{
	if (dN[loc].st == lt && dN[loc].ed == rt) {
		if (dN[loc].min < *low) *low = dN[loc].min;
		if (dN[loc].max > *high) *high = dN[loc].max;
		return;
	}

	if (dN[dN[loc].lt].st <= lt && rt <= dN[dN[loc].lt].ed)
		task_findNod(dN[loc].lt, lt, rt, low, high, dN);
	else if (dN[dN[loc].rt].st <= lt && rt <= dN[dN[loc].rt].ed)
		task_findNod(dN[loc].rt, lt, rt, low, high, dN);
	else if (dN[dN[loc].lt].st <= lt && rt >= dN[dN[loc].rt].st) {
		task_findNod(dN[loc].lt, lt, dN[dN[loc].lt].ed, low, high, dN);
		task_findNod(dN[loc].rt, dN[dN[loc].rt].st, rt, low, high, dN);
	}
}