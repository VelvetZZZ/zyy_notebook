//交换变量
#include <stdio.h>

int main()
{

    int a=5;
    int b=6;
    int t;

    t=a;
    a=b;
    b=t;
    printf("a=%d, b=%d\n", a, b);
    return 0;
}
//套路：
//1.定义一个临时变量t，来存储a的值。
//2.将b的值赋给a，这样a就得到了b的值。
//3.将t的值赋给b，这样b就得到了a原来的值。最后输出交换后的结果。