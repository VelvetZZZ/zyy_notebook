# include <stdio.h>

int main() {
    int a;
    int b;

    printf("请输入两个整数：");
    scanf("%d %d", &a, &b);
    printf("%d + %d = %d\n", a, b, a + b);// %d是一个占位符，表示一个整数，scanf函数会将用户输入的整数存储到变量a和b中，然后printf函数会将a和b的值替换掉%d占位符，输出结果。

    return 0;

}