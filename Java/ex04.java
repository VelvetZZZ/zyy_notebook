import java.util.Scanner;

public class ex04 {
    public static void main(String[] args){
       String a1 = "中";//这是字符串类型
       char a2 = '中';//这是字符类型
       //String a2 = '中'将汇报类型转换错误
       String b1 = "123";//这是字符串类型
       int b2 = 123;//这是整型（只和有没有""有关和数字本身无关）
       //int b3 = "123"将汇报类型转换错误
       String c1 = "true";//这是字符串类型
       boolean c2 = true;//这是布尔型,布尔值true和字符串"true"是完全不同的两个值
        //String e = Hello;//错误，没有双引号
       Scanner scanner = new Scanner(System.in);
        String put = scanner.nextLine();
        System.out.println("您输入的是：");
        System.out.println(put);


    }
}
