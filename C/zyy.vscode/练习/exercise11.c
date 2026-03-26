#include <stdio.h>

int main(){
    //初始化
    int price = 0;
    int bill = 0;

    //读入金额和票面
    printf("请输入金额（元）：");
    scanf("%d", &price);
    printf("请输入票面金额（元）：");
    scanf("%d", &bill);
    //计算找零
    int change = bill - price;
    if (change < 0) {
        printf("票面金额不足。\n");
    } else {
        printf("找零金额为：%d元。\n", change);
    }
}