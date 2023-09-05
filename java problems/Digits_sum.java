import java.util.Scanner;

public class Digits_sum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter digits: ");
        String[] str = sc.nextLine().split("");
        sc.close();
        // int sum = 0;
        // for (String i : str) {
        //     sum += Integer.parseInt(i);
        // }
        // System.out.println("Sum of digits: " + sum);
        int[] arr = new int[str.length];
        for (int i = 0; i < str.length; i++) {
            arr[i] = Integer.parseInt(str[i]);
        }

        for (int i : arr) {
            System.out.println(i);
        }
    }
}
