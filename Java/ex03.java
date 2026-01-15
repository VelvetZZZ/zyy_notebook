public class ex03 {

    public static void main(String[] args){

        char a = 'c'; // 正确
        char b = '中'; // 正确
        char c ='?'; // 正确
        // char d = 'ab'; // 错误，char只能存储单个字符
        //char e = 中; // 错误，必须使用单引号
        //char f ="中"; // 错误，必须使用单引号
        char g = 65; // 正确，65是'A'的Unicode码
        char h = '\u0041'; // 正确，\u0041是'A'的Unicode码,后面必须跟4位16进制数
        char i = 65535; // 正确，char的取值范围是0~65535
        System.out.println(h);
    }
}
