import java.math.BigInteger;

public class Fibonacci {
	public Fibonacci(int m) {
		BigInteger[] array = new BigInteger[m];
		array[0] = BigInteger.valueOf(1);
		array[1] = BigInteger.valueOf(1);
		for (int i = 2; i < m; i++) {
			array[i] = BigInteger.valueOf(0);
			array[i] = array[i].add(array[i - 2]);
			array[i] = array[i].add(array[i - 1]);
		}
		System.out.println("斐波那契数列的前" + m + "个数字为：");
		for (int i = 0; i < m; i++) {
			System.out.println(array[i]);
		}
	}

	String toString(BigInteger array) {
		return array.toString();
	}

	public static void main(String[] args) {
		new Fibonacci(100);

	}

}
