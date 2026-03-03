public class ex09 {
    public static void main(String[] args) {
        //计算1+3+5+...+99的和
        
        int sum = 0;
        int num = 1;
        while (num <= 99){
            if (num % 2 == 1) {
            sum += num;
        }
        num++;
    }
     System.out.println(sum);
}
} 

