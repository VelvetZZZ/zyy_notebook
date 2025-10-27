# C语言除法操作笔记 (对比 Python)

本文简明了 C 语言中除法 / 的行为，并与 Python 进行对照。

## 一、C 语言中 / 操作符的行为

操作式	结果	类型	说明
7 / 2	3	int	整数除法，自动去除小数部分
(float)7 / 2	3.5	float	手动带有浮点类型
7.0 / 2	3.5	double	定值包含浮点，自动解释
7 % 2	1	int	取余运算


⸻

## 二、Python 中相关操作对照

Python 操作	说明
/	始终返回浮点类型结果
//	地板除（向下取整）
%	取余操作


⸻

## 三、易混淆点

需求	C 中写法	Python 中写法
正常除法	(float)a / b	a / b
整除	a / b	a // b
取余	a % b	a % b

记住：C 语言 没有 //！整除需要依靠数据类型定性。

⸻

## 四、实际示例

#include <stdio.h>

int main() {
    int a = 7, b = 2;

    printf("=== C语言除法行为对比 ===\n");
    printf("1. a / b = %d (int / int)\n", a / b);
    printf("2. (float)a / b = %f (float/int)\n", (float)a / b);
    printf("3. 7.0 / 2 = %f (double/int)\n", 7.0 / 2);
    printf("4. a %% b = %d (int %% int)\n", a % b);

    return 0;
}


⸻

## 五、%d 是什么？

格式符	描述	应对类型
%d	整数输出	int
%f	小数输出	float / double
%c	单个字符	char
%s	字符串输出	char[]

%d 是最基本的整数输出，使用 printf() 时必备知识点。

⸻

## 六、必备结论

C语言中 / 是整除还是浮点除，规则是看操作数的类型！

记得：
	•	int / int → 整除（去小数部分）
	•	float / int 或 float / float → 浮点除
	•	没有 //，需要想要就用 int / int

⸻