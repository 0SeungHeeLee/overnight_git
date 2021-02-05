#include <iostream>
#include <stdio.h>
using namespace std;

void tmp(int** arr)
{
	int** ptr = nullptr;
	ptr = new int* [2]; for (int i = 0; i < 2; i++) ptr[i] = new int[3];
	for (int i = 0; i < 2; i++) std::copy(arr[i], arr[i] + 3, ptr[i]);

	arr[1][1] = 100;

	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 3; j++)
			printf("%d ", arr[i][j]);
		printf("\n");
	}
	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 3; j++)
			printf("%d ", ptr[i][j]);
		printf("\n");
	}

	for (int i = 0; i < 2; i++) delete[] ptr[i];
	delete[] ptr;
}
int main()
{
	int** arr = nullptr;
	int** ptr = nullptr;
	arr = new int* [2]; for (int i = 0; i < 2; i++) arr[i] = new int[3];
	for (int i = 0; i < 2; i++)for (int j = 0; j < 3; j++) arr[i][j] = i + j;

	tmp(arr);

	for (int i = 0; i < 2; i++) delete[] arr[i];
	delete[] arr;
}