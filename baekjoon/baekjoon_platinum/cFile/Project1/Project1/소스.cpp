#include <stdlib.h>
#include <iostream>
#include <stdio.h>
using namespace std;

bool map_chk[20][20] = { false };

int main()
{
	int map_size;
	int* map_inf;

	scanf("%d", &map_size);
	map_inf = (int*)malloc(sizeof(int) * map_size);
	for (int i = 0; i < map_size; i++) map_inf[i] = (int)malloc(sizeof(int) * map_size);

	for (int i = 0; i < map_size; i++) {
		for (int i = 0; i < map_size; i++) {

		}
	}

	for (int i = 0; i < map_size; i++) free(map_inf[i]);
	free(map_inf);
}