package practice.day01;

public class VariableDemo {
	//主入口
	public static void main(String[] args) {
		//1.基本用法
		//定义变量，再进行输出
		int a = 10;
		System.out.println(a);//10
		System.out.println(a);//10
		System.out.println(a);//10
		
		//2.变量参与计算
		int b = 30;//注意变量名不能重复
		int c = 20;
		System.out.println(c + b);
		
		//3.修改变量记录的值
		a = 50;
		System.out.println(a);
		
		
		
		//注意事项
		//1.在一条语句中，可以定义多个变量
		int d = 100, e = 200, f = 300;
		System.out.println(d);
		System.out.println(e);
		System.out.println(f);

		//2.变量在使用之前必须赋值
		//int g;
		//g =500
		//建议：以后在定义变量的时候，请直接赋值
		//不要把赋值分开写。
		

	}

}
