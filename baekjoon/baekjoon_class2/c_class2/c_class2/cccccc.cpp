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