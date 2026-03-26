#include <stdio.h>

int main() {
    int type;
    printf("请输入类型（1-3）：");
    scanf("%d", &type);

    switch( type ) {
    case 1:
        // 处理类型1的情况2
        break;
    case 2:
        // 处理类型2的情况
        break;
    case 3:
        // 处理类型3的情况
        break;
    default:
        // 处理其他情况
        break;
}
    return 0;
}