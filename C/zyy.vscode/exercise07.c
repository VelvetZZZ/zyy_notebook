#include <stdio.h>

int main() {
    printf("请分别输入身高的英尺和英寸，"
    "如输入\"5 7\"表示5英尺7英寸：");

    int foot;
    int inch;
    scanf("%d %d", &foot, &inch);

    printf("身高是%f米。\n",
        ((foot + inch / 12.0) * 0.3048));//12.0是一个浮点数,C语言中整数除以整数会得到一个整数，所以需要将12转换为浮点数，才能得到正确的结果。
}