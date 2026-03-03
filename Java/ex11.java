public class ex11 {
    //计算1+3+5+...+99的和
    public static void main(String[] args) {
        int sum = 0;
        for (int num = 1; num <= 99;num += 2) {
            sum += num;
        }
        System.out.println(sum);
    
    }
    
}
