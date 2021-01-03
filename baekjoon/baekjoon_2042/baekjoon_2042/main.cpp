#include <stdio.h>
#include <stdlib.h>

#define TRUE 1
#define FALSE 0
#define NOT_EXIST -123456

typedef struct value {
	int st;			//시작 범위
	int ed;			//끝 범위
	long long sum;		//합
	int lt;		//좌측노드 주소
	int rt;		//우측노드 주소
}val;
typedef struct task {
	int loot;		//경우의 수
	int st_ord;		//시작 범위
	int ed_chg;		//끝 범위
}tsk;
typedef const int cint;

long long func_sum(cint lt, cint rt, int* arr);

void task_findAns(cint sV, cint sT, int* dV, tsk* dT, val* dN);
void task_getValue(int loc, long long* res, cint st, cint ed, cint sV, val* dN);

int main()
{
	int size_value;
	int size_change;	
	int size_sum;
	int* data_value;		//숫자 저장
	tsk* data_task;			//작업 저장
	val* data_nod;			//이진 노드 (ORDER => QUEUE 사용)

	scanf("%d %d %d", &size_value, &size_change, &size_sum);
	data_value = (int*)malloc(sizeof(int) * (size_value + 1));
	data_task = (tsk*)malloc(sizeof(tsk) * (size_change + size_sum + 1));
	data_nod = (val*)malloc(sizeof(val) * (size_value * 5));
	for (int i = 1; i <= size_value; i++)
		scanf("%d", &data_value[i]);
	for (int i = 1; i <= size_change + size_sum; i++)
		scanf("%d %d %d", &data_task[i].loot, &data_task[i].st_ord, &data_task[i].ed_chg);
	task_findAns(size_value, size_change + size_sum, data_value, data_task, data_nod);

	free(data_value);
	free(data_task);
	free(data_nod);

	return 0;
}

long long func_sum(cint lt, cint rt, int* arr)
{
	long long tmp;
	tmp = 0;
	for (int i = lt; i <= rt; i++)
		tmp	+= arr[i];

	return tmp;
}
void task_findAns(cint sV, cint sT, int* dV, tsk* dT, val* dN)
{
	int* queue_log = (int*)malloc(sizeof(int) * sV * 5);
	int cnt_st;
	int cnt_ed;
	long long tmp_value;
	int tmp_loc;

	queue_log[1] = 0;
	dN[1].st = cnt_st = cnt_ed = 1;
	dN[1].ed = sV;
	dN[1].sum = func_sum(1, sV, dV);
	dN[1].lt = ++cnt_ed;
	queue_log[cnt_ed] = 1;
	dN[1].rt = ++cnt_ed;
	queue_log[cnt_ed] = 1;

	if(sV > 1) while (++cnt_st <= cnt_ed) {
		if (queue_log[cnt_st] == NOT_EXIST) continue;

		if (cnt_st % 2 == 0) {
			dN[cnt_st].st = dN[queue_log[cnt_st]].st;
			dN[cnt_st].ed = (dN[queue_log[cnt_st]].st + dN[queue_log[cnt_st]].ed) / 2;
		}	//ex. 1 ~ 10 -> 1 ~ 5
		else if (cnt_st % 2 == 1) {
			dN[cnt_st].st = (dN[queue_log[cnt_st]].st + dN[queue_log[cnt_st]].ed) / 2 + 1;
			dN[cnt_st].ed = dN[queue_log[cnt_st]].ed;
		}	//ex. 1 ~ 10 -> 6 ~ 10

		dN[cnt_st].sum = func_sum(dN[cnt_st].st, dN[cnt_st].ed, dV);	//합 구하기

		if (dN[cnt_st].st != dN[cnt_st].ed) {
			dN[cnt_st].lt = ++cnt_ed;
			queue_log[cnt_ed] = cnt_st;
			dN[cnt_st].rt = ++cnt_ed;
			queue_log[cnt_ed] = cnt_st;
		}
		else {
			dN[cnt_st].lt = NOT_EXIST;
			dN[cnt_st].rt = NOT_EXIST;
		}
		//노드 경로 결정
	}

	for (int i = 1; i <= sT; i++) {
		if (dT[i].loot == 1) {
			tmp_loc = 1;

			while (dN[tmp_loc].st != dN[tmp_loc].ed) {
				dN[tmp_loc].sum -= (dV[dT[i].st_ord] - dT[i].ed_chg);
				if (dN[dN[tmp_loc].lt].st <= dT[i].st_ord && dT[i].st_ord <= dN[dN[tmp_loc].lt].ed)
					tmp_loc = dN[tmp_loc].lt;
				else
					tmp_loc = dN[tmp_loc].rt; 
			}
			dN[tmp_loc].sum -= (dV[dT[i].st_ord] - dT[i].ed_chg);
			dV[dT[i].st_ord] = dT[i].ed_chg;
		}	//change

		else if (dT[i].loot == 2) {
			tmp_value = 0;

			task_getValue(1, &tmp_value, dT[i].st_ord, dT[i].ed_chg, sV, dN);
			printf("%lld\n", tmp_value);
		}	//sum
	}

	free(queue_log);
}
void task_getValue(int loc, long long* res, cint st, cint ed, cint sV, val* dN)
{
	if (dN[loc].st == st && dN[loc].ed == ed) {
		*res += dN[loc].sum;
		return;
	}

	if (dN[dN[loc].lt].st <= st && ed <= dN[dN[loc].lt].ed) {
		task_getValue(dN[loc].lt, res, st, ed, sV, dN);
	}// [----(____)----]
	else if (dN[dN[loc].rt].st <= st && ed <= dN[dN[loc].rt].ed) {
		task_getValue(dN[loc].rt, res, st, ed, sV, dN);
	}// [----(____)----] 
	else if (dN[dN[loc].lt].st <= st && ed > dN[dN[loc].lt].ed) {
		task_getValue(dN[loc].lt, res, st, dN[dN[loc].lt].ed, sV, dN);
		task_getValue(dN[loc].rt, res, dN[dN[loc].rt].st, ed, sV, dN);
	}// [---(____][___)------]
}

/*
void main() {
	int arrsize;
	int mod;
	int mod2;
	int cal;
	int cal2;

	int* arr;
	int* calarr;
	int buff;
	int buff2;
	int buff3;
	int index = 0;

	scanf_s("%d %d %d", &arrsize, &mod, &cal);

	mod2 = mod;
	cal2 = cal;

	arr = (int*) calloc(arrsize, sizeof(int));
	calarr = (int*) calloc(cal, sizeof(int));

	for (int i = 0; i < arrsize; i++)
	{
		scanf_s("%d", &arr[i]);
	}
	
	for (int i = 0; i < mod2 + cal2; i++)
	{
		scanf_s("%d %d %d", &buff, &buff2, &buff3);
		if (buff == 1)
		{
			if (mod - 1 <= -1)
			{
				return; // 명령 가능 횟수 초과
			}
			else
			{
				arr[buff2 - 1] = buff3;
				mod--;
			}
		}
		if (buff == 2)
		{
			if (cal - 1 <= -1)
			{
				return; // 명령 가능 횟수 초과
			}
			else
			{
				for (int j = buff2 - 1; j < buff3; j++)
				{
					calarr[index] += arr[j];
				}
				index++;
			}
		}
	}	

	for (int i = 0; i < cal2; i++)
	{
		printf("%d\n", calarr[i]);
	}

	return;
}
*/