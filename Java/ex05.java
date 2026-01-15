public class ex05 {
    public static void main(String[] args) {
        double doubleNum = 3.14;
        //强制类型转换，把double类型转换为int类型，舍弃小数部分（是舍弃，不是四舍五入）
        int intNum = (int)doubleNum;//强制类型转换，值为3，小数点后的部分被舍弃
        System.out.println(intNum);
        byte byteNum = (byte) intNum;//强制类型转换，把int类型转换为byte类型,值为3
        System.out.println(byteNum);
        int intNum2 = 129;
        byte byteNum2 = (byte) intNum2;//强制类型转换，把int类型转换为byte类型，值为-127，超出byte范围部分被舍弃
        System.out.println(byteNum2);
    
    char charA = 'A';//字符'A'，对应的Unicode码值为65
    int b = a + 1;//把char类型转换为int类型，值为66

    int c = 10;
    double d = c +3.14;//把int类型转换为double类型，值为13.14
    System.out.println("hello" + 123);
    
    
    }
}
