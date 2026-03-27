#include <stdio.h>

int main(){
    int x;
    int n=0;

    scanf("%d", &x);

    n++;
    x /= 10;

    while (x > 0){
        n++;
        x /= 10;
    }

    printf("数字的位数是：%d\n", n);
    return 0;
}