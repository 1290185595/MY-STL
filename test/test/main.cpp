//
// Created by t1290 on 2023/2/17.
//
#include "std.h"

vector<int>&& test() {
    static vector<int> x= {1,2}, &y=x;
    x.push_back(1);
    return move(y);
}

int main(){
    auto x = test(), y = test();
    cout << x.size();
    cout << __has_trivial_destructor(int);
}