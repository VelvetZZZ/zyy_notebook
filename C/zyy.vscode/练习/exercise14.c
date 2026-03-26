#include <stdio.h>

int main() {1
    int type;
    printf("请输入类型（1-4）：");
    scanf("%d", &type);
    switch(type) {
    case 1:
    case 2:
        printf("你好！\n");
        break;
    case 3:
        printf("晚上好！\n");
    case 4:
        printf("再见！\n");
        break;
    default:
        printf("输入错误！\n");
        break;
}
    return 0;
}