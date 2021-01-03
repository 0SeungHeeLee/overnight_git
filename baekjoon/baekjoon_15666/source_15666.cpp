#include <stdio.h>
#include <stdlib.h>

#define MX 10000

int compare(const void *a, const void *b);
void find_arr(int order, int info, int* arr, int size, int* ans, int num);

int main()
{
	int num_natural;
	int num_select;
	int chk_element[MX] = { 0 };
	int* arr_element;
	int* arr_ans;
	int size_element = 0;
	int tmp_element;

	scanf("%d %d", &num_natural, &num_select);
	arr_element = (int*)malloc(sizeof(int));
	arr_ans = (int*)malloc(sizeof(int) * num_select);

	for (int i = 0; i < num_natural; i++) {
		//중복 여부 확인
		scanf("%d", &tmp_element);
		if (chk_element[tmp_element] == 1) continue;
		
		//원소 추가
		chk_element[tmp_element] = 1;
		arr_element = (int*)realloc(arr_element, sizeof(int)*(size_element + 1));
		arr_element[size_element++] = tmp_element;
	}

	qsort(arr_element, size_element, sizeof(int), compare);
	find_arr(0, 0, arr_element, size_element, arr_ans, num_select);

	free(arr_element);
	free(arr_ans);
}

int compare(const void *a, const void *b)
{
	int num1 = *(int *)a; 
	int num2 = *(int *)b; 
	if (num1 < num2) return -1;
	if (num1 > num2) return 1;
	return 0;
}
void find_arr(int order, int info, int* arr, int size, int* ans, int num)
{
	ans[order] = arr[info];
	if (order == num - 1) {
		for (int i = 0; i < num; i++)
			printf("%d ", ans[i]);
		printf("\n");
	}

	if (order + 1 < num) find_arr(order + 1, info, arr, size, ans, num);
	if(info + 1 < size) find_arr(order, info + 1, arr, size, ans, num);
}