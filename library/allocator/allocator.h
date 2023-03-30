//
// Created by t1290 on 2023/2/17.
//

#ifndef MY_STL_ALLOCATOR_H
#define MY_STL_ALLOCATOR_H

#include <iostream>
namespace MySTL {
    template<typename T>
    class allocator {
    public:
        allocator();
    };

}
template<typename T>
MySTL::allocator<T>::allocator() {
    std::cout << 1;
}
#endif //MY_STL_ALLOCATOR_H
