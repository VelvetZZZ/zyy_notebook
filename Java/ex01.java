public class ex01 {
    public static void main(String[] args) {
        byte a = 10;//正确
        //byte b = 128;//错误，超出byte范围
        short c = 20000;//正确
        //short d = 40000;//错误，超出short范围
        int e = 300000000;//正确
        //int f = 4000000000;//错误，超出int范围
        long g = 4000000000L;//正确，注意后缀L
        //long h = 9000000000;//错误，超出int范围，必须加后缀L
        

        int h = 0b11;//二进制表示的3
        int i = 023;//八进制表示的19
        int j = 0x1F;//十六进制表示的31
    }
}

