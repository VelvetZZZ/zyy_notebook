# include <stdio.h>

int main() {

    const int AMOUNT = 100;//const是一个修饰符，给变量加上不变的属性，修饰的变量必须在定义时初始化，且之后不能修改其值，否则会导致编译错误。
    int price = 0;

    // AMOUNT = 90;

    printf("请输入金额（元）：");
    scanf("%d", &price);

    int change = AMOUNT - price;

    printf("找您%d元。\n", change);

    return 0;
}