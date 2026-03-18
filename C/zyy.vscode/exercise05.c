# include <stdio.h>

int main() {

    int amount = 100;
    int price = 0;

    
    printf("请输入金额（元）：");
    scanf("%d", &price);

    printf("请输入票面金额（元）：");
    scanf("%d", &amount);// 这里的amount是一个变量，之前定义的amount是一个常量，不能修改，所以这里重新定义了一个变量amount来存储用户输入的票面金额。

    int change = amount - price;

    printf("找您%d元。\n", change);

    return 0;
}