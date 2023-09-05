import java.util.Scanner;

public class Sum_even_oddDigits {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter digits: ");
        String[] str = sc.nextLine().split("");
        sc.close();
        int[] arr = new int[str.length];
        for (int i = 0; i < str.length; i++) {
            arr[i] = Integer.parseInt(str[i]);
        }
        int sum_even = 0;
        int sum_odd = 0;
        for (int i=str.length; i>0; i--) {
            int pos = str.length - i + 1;
            if (pos % 2 == 1) {
                sum_odd += arr[i-1];
            } else {
                sum_even += arr[i-1];
            }
        }
        
        System.out.println("Sum of odd digits: " + sum_odd);
        System.out.println("Sum of even digits: " + sum_even);

    }
}
