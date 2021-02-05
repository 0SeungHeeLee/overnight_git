#include <stdlib.h>
#include <iostream>
#include <stdio.h>
using namespace std;

int val_max = 0;
int val_size;
int val_size_1;
int val_size_2;
int inf_dir[4][2] = { {1,0},{-1,0},{0,1},{0,-1} };
int chk[20][20] = { 0 };
int val_chkLim = 11;
int val_tries = 10;

void task_play(int**, int);
bool task_chkCanMove(int**, int);
bool task_chkDifferent(int**, int**);
void task_shiftBlock(int**, int);
int task_findMax(int**);

int main()
{
	int map_size;
	int** map_inf;
	int tmp;

	scanf("%d", &map_size);
	map_inf = new int* [map_size];
	for (int i = 0; i < map_size; i++) map_inf[i] = new int[map_size];
	for (int i = 0; i < map_size; i++) for (int j = 0; j < map_size; j++) scanf("%d", &map_inf[i][j]);

	val_size = map_size;
	val_size_1 = map_size - 1;
	val_size_2 = map_size - 2;
	tmp = task_findMax(map_inf);
	task_play(map_inf, 1);
	if (!val_max) val_max = tmp;

	printf("%d", val_max);

	for (int i = 0; i < map_size; i++) delete[] map_inf[i];
	delete[] map_inf;

	return 0;
}
void task_play(int** map_inf, int val_turn)
{
	int tmp_max;
	int** map_copy;
	map_copy = nullptr;

	if (val_turn > val_tries) {
		tmp_max = task_findMax(map_inf);
		val_max = val_max < tmp_max ? tmp_max : val_max;
		return;
	}
	if (task_chkCanMove(map_inf, val_turn)) return;

	for (int i = 0; i < 4; i++) {
		map_copy = new int* [val_size]; for (int j = 0; j < val_size; j++) map_copy[j] = new int[val_size];
		for (int j = 0; j < val_size; j++) std::copy(map_inf[j], map_inf[j] + val_size, map_copy[j]);
		task_shiftBlock(map_copy, i);
		if (task_chkDifferent(map_inf, map_copy)) task_play(map_copy, val_turn + 1);
		for (int j = 0; j < val_size; j++) delete[] map_copy[j];
		delete[] map_copy;
	}
}
bool task_chkCanMove(int** arr, int turn)
{
	int tmp_max;
	int tmp_sum;
	int tmp_lim;
	int tmp_cnt;
	
	tmp_max = 0;
	tmp_sum = 0;

	for (int i = 0; i < val_size; i++)
		for (int j = 0; j < val_size; j++) {
			tmp_sum += arr[i][j];
			if (tmp_max < arr[i][j]) tmp_max = arr[i][j];
		}

	if (val_max){
		tmp_lim = val_max;
		tmp_cnt = val_chkLim - turn;
		while(tmp_cnt--) tmp_lim /= 2;
		if (tmp_lim >= tmp_max) return true;
	}

	if (tmp_max * 2 > tmp_sum) {
		if (val_max < tmp_max) val_max = tmp_max;
		return true;
	}
	return false;
}
bool task_chkDifferent(int** base, int** copy)
{
	for (int i = 0; i < val_size; i++)
		for (int j = 0; j < val_size; j++)
			if (base[i][j] != copy[i][j]) return true;
	return false;
}
void task_shiftBlock(int** map_inf, int trigger)
{
	int addX, addY;
	int cX, cY;

	for (int i = 0; i < val_size; i++) for (int j = 0; j < val_size; j++) chk[i][j] = 0;
	addY = inf_dir[trigger][0]; addX = inf_dir[trigger][1];

	if (addY == 1) {
		for (int y = val_size_2; y >= 0; y--)
			for (int x = 0; x < val_size; x++){
				if (!map_inf[y][x]) continue;
				cY = y;
				while (cY < val_size_1 && !map_inf[cY + 1][x]) cY++;
				if (cY < val_size_1 && map_inf[y][x] == map_inf[cY + 1][x] && !chk[cY][x]) {
					map_inf[cY + 1][x] *= 2;
					map_inf[y][x] = 0;
					chk[cY][x] = 1;
				}
				else if (!map_inf[cY][x]) {
					map_inf[cY][x] = map_inf[y][x];
					map_inf[y][x] = 0;
				}
			}
	}
	else if (addY == -1) {
		for (int y = 1; y < val_size; y++)
			for (int x = 0; x < val_size; x++) {
				if (!map_inf[y][x]) continue;
				cY = y;
				while (cY >= 1 && !map_inf[cY - 1][x]) cY--;
				if (cY >= 1 && map_inf[y][x] == map_inf[cY - 1][x] && !chk[cY][x]) {
					map_inf[cY - 1][x] *= 2;
					map_inf[y][x] = 0;
					chk[cY][x] = 1;
				}
				else if (!map_inf[cY][x]) {
					map_inf[cY][x] = map_inf[y][x];
					map_inf[y][x] = 0;
				}
			}
	}
	else if (addX == 1) {
		for (int x = val_size_2; x >= 0; x--)
			for (int y = 0; y < val_size; y++) {
				if (!map_inf[y][x]) continue;
				cX = x;
				while (cX < val_size_1 && !map_inf[y][cX + 1]) cX++;
				if (cX < val_size_1 && map_inf[y][x] == map_inf[y][cX + 1] && !chk[y][cX]) {
					map_inf[y][cX + 1] *= 2;
					map_inf[y][x] = 0;
					chk[y][cX] = 1;
				}
				else if (!map_inf[y][cX]) {
					map_inf[y][cX] = map_inf[y][x];
					map_inf[y][x] = 0;
				}
			}
	}
	else if (addX == -1) {
		for (int x = 1; x < val_size; x++)
			for (int y = 0; y < val_size; y++) {
				if (!map_inf[y][x]) continue;
				cX = x;
				while (cX >= 1 && !map_inf[y][cX - 1]) cX--;
				if (cX >= 1 && map_inf[y][x] == map_inf[y][cX - 1] && !chk[y][cX]) {
					map_inf[y][cX - 1] *= 2;
					map_inf[y][x] = 0;
					chk[y][cX] = 1;
				}
				else if (!map_inf[y][cX]) {
					map_inf[y][cX] = map_inf[y][x];
					map_inf[y][x] = 0;
				}
			}
	}
}
int task_findMax(int** arr)
{
	int tmp;

	tmp = 0;
	for (int i = 0; i < val_size; i++) for (int j = 0; j < val_size; j++) tmp = tmp < arr[i][j] ? arr[i][j] : tmp;
	return tmp;
}