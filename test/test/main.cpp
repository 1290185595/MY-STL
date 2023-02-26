//
// Created by t1290 on 2023/2/17.
//
#include "std.h"
int main(){
    vector<int> a = {14,2,4,12,3};
    auto p = a.begin(), q = p+1;
    sort(p, a.end());
    cout << *p << *q;
}