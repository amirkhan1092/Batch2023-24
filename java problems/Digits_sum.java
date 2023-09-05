import java.util.Scanner;

public class Digits_sum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter digits: ");
        String[] str = sc.nextLine().split("");
        sc.close();
        int sum = 0;
        for (String i : str) {
            sum += Integer.parseInt(i);
        }
        System.out.println("Sum of digits: " + sum);
    }
}
