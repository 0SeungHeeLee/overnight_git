//19235
#include <stdio.h>

#define MAX_BLOCK 10000
#define LEN_LONG 10
#define LEN_SHORT 4

typedef struct {
	int case_block;
	int loc_x;
	int loc_y;
} blk;

int shape_block[3][2] = { {0,0},{0,1},{1,0} };

void task_setBlockLoc(int mVer[][LEN_LONG], int mHor[][LEN_SHORT], int cBlock, int lX, int lY);
void task_removeBlock(int mVer[][LEN_LONG], int mHor[][LEN_SHORT], int* vScore);
int task_cntBlock(int mVer[][LEN_LONG], int mHor[][LEN_SHORT]);
void testing(int mVer[][LEN_LONG], int mHor[][LEN_SHORT], int num);

int main()
{
	int value_score = 0;
	int try_drop;
	blk info_block[MAX_BLOCK];
	int map_ver[LEN_SHORT][LEN_LONG] = { 0 };
	int map_hor[LEN_LONG][LEN_SHORT] = { 0 };

	scanf("%d", &try_drop);
	for (int i = 0; i < try_drop; i++)
		scanf("%d %d %d", &info_block[i].case_block, &info_block[i].loc_x, &info_block[i].loc_y);

	for (int i = 0; i < try_drop; i++) {
		task_setBlockLoc(map_ver, map_hor, info_block[i].case_block - 1, info_block[i].loc_x, info_block[i].loc_y);
		//testing(map_ver, map_hor, i + 1);
		task_removeBlock(map_ver, map_hor, &value_score);
		//testing(map_ver, map_hor, i + 1);
	}
	printf("%d\n%d", value_score, task_cntBlock(map_ver, map_hor));
	//testing(map_ver, map_hor, 100000);
}

void task_setBlockLoc(int mVer[][LEN_LONG], int mHor[][LEN_SHORT], int cBlock, int lX, int lY)
{
	int llX;
	int llY;
	int cnt;

	llX = lX + shape_block[cBlock][0];
	llY = lY + shape_block[cBlock][1];

	cnt = 0;
	while (mVer[lX][lY + cnt + 1] == 0 && mVer[llX][llY + cnt + 1] == 0 && llY + cnt + 1 < LEN_LONG)
		cnt++;
	mVer[lX][lY + cnt] = mVer[llX][llY + cnt] = 1;

	cnt = 0;
	while (mHor[lX + cnt + 1][lY] == 0 && mHor[llX + cnt + 1][llY] == 0 && llX + cnt + 1 < LEN_LONG)
		cnt++;
	mHor[lX + cnt][lY] = mHor[llX + cnt][llY] = 1;
}
void task_removeBlock(int mVer[][LEN_LONG], int mHor[][LEN_SHORT], int* vScore)
{
	int loc_remove;
	int tmp_remove;
	int tmp_loc;
	int chkArr[10];

	while (1) {
		loc_remove = 10;
		for (int i = 0; i < 10; i++)
			chkArr[i] = 0;
		for (int i = 9; i >= 4; i--) {
			tmp_remove = 0;
			for (int j = 0; j < 4; j++)
				tmp_remove += mVer[j][i];
			if (tmp_remove == 4) {
				chkArr[i] = 1;
				if (loc_remove == 10) loc_remove = i;
			}
		}

		if (loc_remove == 10) break;

		for (int i = 9; i >= 4; i--)
			if (chkArr[i] == 1) {
				for (int j = 0; j < 4; j++)
					mVer[j][i] = 0;
				*vScore += 1;
			}

		for (int i = loc_remove - 1; i >= 4; i--)
			for (int j = 0; j < 4; j++) {
				if (mVer[j][i] == 0) continue;
				mVer[j][i] = 0;
				tmp_loc = i;
				while (mVer[j][tmp_loc + 1] == 0 && tmp_loc + 1 < LEN_LONG)
					tmp_loc++;
				mVer[j][tmp_loc] = 1;
			}
	}
	loc_remove = 0;
	for (int i = 0; i < 4; i++)
		if (mVer[i][5] == 1) loc_remove = 1;
	for (int i = 0; i < 4; i++)
		if (mVer[i][4] == 1) loc_remove = 2;
	if (loc_remove != 0) {
		for (int i = 9; i > 9 - loc_remove; i--)
			for (int j = 0; j < 4; j++)
				mVer[j][i] = 0;
		for (int i = 9 - loc_remove; i >= 4; i--)
			for (int j = 0; j < 4; j++) {
				if (mVer[j][i] == 0) continue;
				mVer[j][i] = 0;
				mVer[j][i + loc_remove] = 1;
			}
	}

	while (1) {
		loc_remove = 10;
		for (int i = 0; i < 10; i++)
			chkArr[i] = 0;
		for (int i = 9; i >= 4; i--) {
			tmp_remove = 0;
			for (int j = 0; j < 4; j++)
				tmp_remove += mHor[i][j];
			if (tmp_remove == 4) {
				chkArr[i] = 1;
				if (loc_remove == 10) loc_remove = i;
			}
		}

		if (loc_remove == 10) break;

		for (int i = 9; i >= 4; i--)
			if (chkArr[i] == 1) {
				for (int j = 0; j < 4; j++)
					mHor[i][j] = 0;
				*vScore += 1;
			}
		for (int i = loc_remove - 1; i >= 4; i--)
			for (int j = 0; j < 4; j++) {
				if (mHor[i][j] == 0) continue;
				mHor[i][j] = 0;
				tmp_loc = i;
				while (mHor[tmp_loc + 1][j] == 0 && tmp_loc + 1 < LEN_LONG)
					tmp_loc++;
				mHor[tmp_loc][j] = 1;
			}
	}
	loc_remove = 0;
	for (int i = 0; i < 4; i++)
		if (mHor[5][i] == 1) loc_remove = 1;
	for (int i = 0; i < 4; i++)
		if (mHor[4][i] == 1) loc_remove = 2;
	if (loc_remove != 0) {
		for (int i = 9; i > 9 - loc_remove; i--)
			for (int j = 0; j < 4; j++)
				mHor[i][j] = 0;
		for (int i = 9 - loc_remove; i >= 4; i--)
			for (int j = 0; j < 4; j++) {
				if (mHor[i][j] == 0) continue;
				mHor[i][j] = 0;
				mHor[i + loc_remove][j] = 1;
			}
	}
}
int task_cntBlock(int mVer[][LEN_LONG], int mHor[][LEN_SHORT])
{
	int cnt = 0;

	for (int i = 9; i >= 6; i--)
		for (int j = 0; j < 4; j++) {
			cnt += mVer[j][i];
			cnt += mHor[i][j];
		}

	return cnt;
}

void testing(int mVer[][LEN_LONG], int mHor[][LEN_SHORT], int num)
{
	printf("\n%d Trying\n", num);
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j <= 9; j++)
			printf("%d ", mVer[i][j]);
		printf("\n");
	}
	for (int i = 4; i <= 9; i++) {
		for (int j = 0; j < 4; j++)
			printf("%d ", mHor[i][j]);
		printf("\n");
	}
	printf("\n");
}

////10866
//#include <stdio.h>
//#include <string>
//#include <iostream>
//#include <cstdlib>
//#include <vector>
//using namespace std;
//
//int main()
//{
//	int task_num;
//	int tmp;
//	string task_str;
//	vector<int> arr;
//
//	cin >> task_num;
//
//	for (int i = 0; i < task_num; i++) {
//		cin >> task_str;
//
//		if (task_str == "push_front") {
//			cin >> tmp;
//			arr.insert(arr.begin(),1,tmp);
//		}
//		else if (task_str == "push_back") {
//			cin >> tmp;
//			arr.push_back(tmp);
//		}
//		else if (task_str == "pop_front") {
//			if (arr.size() > 0) {
//				printf("%d\n", arr.front());
//				arr.erase(arr.begin());
//			}
//			else printf("-1\n");
//		}
//		else if (task_str == "pop_back") {
//			if (arr.size() > 0) {
//				printf("%d\n", arr.back());
//				arr.pop_back();
//			}
//			else printf("-1\n");
//		}
//		else if (task_str == "size") printf("%d\n", arr.size());
//		else if (task_str == "empty") {
//			if (arr.size() == 0) printf("1\n");
//			else printf("0\n");
//		}
//		else if (task_str == "front") {
//			if (arr.size() > 0) printf("%d\n", arr.front());
//			else printf("-1\n");
//		}
//		else {
//			if (arr.size() > 0) printf("%d\n", arr.back());
//			else printf("-1\n");
//		}
//	}
//}

////10845
//#include <stdio.h>
//#include <string>
//#include <iostream>
//#include <cstdlib>
//#include <vector>
//using namespace std;
//
//int main()
//{
//	int task_num;
//	int tmp;
//	string task_str;
//	vector<int> arr;
//
//	cin >> task_num;
//
//	for(int i=0 ; i<task_num ; i++) {
//		cin >> task_str;
//
//		if (task_str == "push") {
//			cin >> tmp;
//			arr.push_back(tmp);
//		}
//		else if (task_str == "pop") {
//			if (arr.size() > 0) {
//				printf("%d\n", arr.front());
//				arr.erase(arr.begin());
//			}
//			else printf("-1\n");
//		}
//		else if (task_str == "size") printf("%d\n", arr.size());
//		else if (task_str == "empty") {
//			if (arr.size() == 0) printf("1\n");
//			else printf("0\n");
//		}
//		else if (task_str == "front") {
//			if (arr.size() > 0) printf("%d\n", arr.front());
//			else printf("-1\n");
//		}
//		else {
//			if (arr.size() > 0) printf("%d\n", arr.back());
//			else printf("-1\n");
//		}
//	}
//}

////10828
//#include <stdio.h>
//#include <string>
//#include <iostream>
//#include <cstdlib>
//#include <vector>
//using namespace std;
//
//int main()
//{
//	int task_num;
//	int tmp;
//	string task_str;
//	vector<int> arr;
//
//	cin >> task_num;
//
//	for(int i=0 ; i<task_num ; i++) {
//		cin >> task_str;
//
//		if (task_str == "push") {
//			cin >> tmp;
//			arr.push_back(tmp);
//		}
//		else if (task_str == "pop") {
//			if (arr.size() > 0) {
//				printf("%d\n", arr.back());
//				arr.pop_back();
//			}
//			else printf("-1\n");
//		}
//		else if (task_str == "size") printf("%d\n", arr.size());
//		else if (task_str == "empty") {
//			if (arr.size() == 0) printf("1\n");
//			else printf("0\n");
//		}
//		else {
//			if (arr.size() > 0) printf("%d\n", arr.back());
//			else printf("-1\n");
//		}
//
//	}
//}


////10816
//#include <stdio.h>
//#include <iostream>
//#include <algorithm>
//
//using namespace std;
//
//int binarySearch(int* arr, int val_find, int val_size);
//int main()
//{
//	int card_num;
//	int card_searchIndex;
//
//	scanf("%d", &card_num);
//	int* card_inf = new int[card_num];
//	for (int i = 0; i < card_num; i++) scanf("%d", &card_inf[i]);
//	scanf("%d", &card_searchIndex);
//	int* card_searchInf = new int[card_searchIndex];
//	for (int i = 0; i < card_searchIndex; i++) scanf("%d", &card_searchInf[i]);
//	
//	sort(card_inf,card_inf+card_num);
//	for (int i = 0; i < card_searchIndex; i++)
//		printf("%d ", binarySearch(card_inf, card_searchInf[i], card_num));
//
//	delete[] card_inf;
//	delete[] card_searchInf;
//	return 0;
//}
//int binarySearch(int* arr, int val_find, int val_size)
//{
//	int st;
//	int ed;
//	int md;
//	int tp;
//	int ts;
//	int te;
//
//	st = 0;
//	ed = val_size - 1;
//
//	while (st <= ed) {
//		md = (st + ed) / 2;
//		if (arr[md] == val_find) break;
//		if (arr[md] < val_find) st = md + 1;
//		else ed = md - 1;
//	}
//	if (st > ed) return 0;
//	tp = md;
//
//	st = 0; 
//	ed = tp;
//	while (st <= ed) {
//		md = (st + ed) / 2;
//		if (arr[md] == val_find) ed = md - 1;
//		else st = md + 1;
//	}
//	ts = st;
//
//	st = tp;
//	ed = val_size -1;
//	while (st <= ed) {
//		md = (st + ed) / 2;
//		if (arr[md] == val_find) st = md + 1;
//		else ed = md - 1;
//	}
//	te = ed;
//	if (arr[te] == val_find) te++;
//	
//	return te - ts;
//}

////2751
//#include <stdio.h>
//#include <stdlib.h>
//#define SWAP(x,y) { int t=x; x=y; y=t; }
//
//void sort_insert(int* a, int st, int ed)
//{
//    for (int i = st; i <= ed; i++)
//        for (int j = i; j > st; j--) {
//            if (a[j] < a[j - 1]) {
//                SWAP(a[j], a[j - 1])
//            }
//            else break;
//        }
//}
//void sort_quick(int* a, int st, int ed)
//{
//    int lt, rt;
//    if (st >= ed) return;
//    if (ed - st <= 500) {
//        sort_insert(a, st, ed);
//        return;
//    }
//    lt = st; rt = ed + 1;
//    while (1) {
//        while (++lt<=ed && a[lt] < a[st]);
//        while (--rt>=st && a[rt] > a[st]);
//        if (lt >= rt) break;
//        SWAP(a[lt], a[rt])
//    }
//    SWAP(a[st], a[rt]);
//
//    sort_quick(a, st, rt - 1);
//    sort_quick(a, rt + 1, ed);
//}
//
//int main()
//{
//    int* a;
//    int k;
//
//    scanf("%d", &k);
//    a = (int*)malloc(sizeof(int)*k);
//    for(int i = 0 ; i < k ; i++) scanf("%d", &a[i]);
//    sort_quick(a, 0, k-1);
//    for (int i = 0; i < k ; i++) printf("%d\n", a[i]);
//
//    free(a);
//    return 0;
//}
//#include <stdio.h>
//#include <iostream>
//#include <algorithm>
//using namespace std;
//
//int main()
//{
//    int* a;
//    int k;
//
//    scanf("%d", &k);
//    a = (int*)malloc(sizeof(int) * k);
//    for (int i = 0; i < k; i++) scanf("%d", &a[i]);
//    sort(a, a + k);
//    for (int i = 0; i < k; i++) printf("%d\n", a[i]);
//
//    free(a);
//    return 0;
//}

// //2164
// #include <stdio.h>
// int main(){ int n,c=1;scanf("%d",&n);while(c*2<n)c*=2;printf("%d",n>1?(n-c)*2:1); }

//#include <stdio.h>
//#include <stdlib.h>
//
//int main()
//{
//	int card_max;
//	int card_num;
//	int* card_inf;
//	int tmp_inf;
//	int loc_st;
//
//	scanf("%d", &card_max);
//	if (card_max == 1) {
//		printf("1");
//		return 0;
//	}
//	card_num = card_max - 1;
//	loc_st = 0;
//	card_inf = (int*)calloc((card_max*2), sizeof(int));
//	for (int i = 0; i < card_max; i++) card_inf[i] = i + 1;
//
//	while (--card_num > 0) {
//		tmp_inf = card_inf[loc_st+1];
//		loc_st += 2;
//		card_inf[loc_st+card_num] = tmp_inf;
//	}
//	printf("%d", card_inf[loc_st+1]);
//
//	free(card_inf);
//	return 0;
//}