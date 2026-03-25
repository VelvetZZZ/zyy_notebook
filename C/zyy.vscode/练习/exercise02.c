#include <stdio.h>

int main() {
    //基本运算
    printf("=== 基本运算 ===\n");
    printf("1 + 2 = %d\n", 1 + 2);
    int a = 7, b = 2;

    printf("=== C语言除法行为对比 ===\n");

    // 整数除法
    printf("1. a / b = %d (int / int)\n", a / b);

    // 浮点除法（强制转换）
    printf("2. (float)a / b = %f (转成浮点数)\n", (float)a / b);

    // 浮点除法（写成浮点字面量）
    printf("3. 7.0 / 2 = %f (float literal)\n", 7.0 / 2);

    // 取余
    printf("4. a %% b = %d (取余)\n", a % b);

    return 0;
}