#include <stdio.h>

void program1() {
    printf("Hello, C!\n");
}

void program2() {
    printf("Hello World!\n");
}

int main() {
    // 调用其中一个
    program1();  // 或者改成 program2();
    program2();

    return 0;
