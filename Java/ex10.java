import java.util.Scanner;
public class ex10 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入整数 n：");
        int n = sc.nextInt();
        
        double sum = 0.0; // 结果必须是 double
        
        // 观察分子：从 1 开始，一直到 n-1
        // 观察分母：总是比分子大 1
        for (int i = 1; i < n; i++) {
            // 核心公式：强制转为 double 进行除法
            sum += i / (i + 1.0);
        }
        
        System.out.println("结果是：" + sum);
    }
}
    
