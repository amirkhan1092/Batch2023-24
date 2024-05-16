package DSA;
import java.util.Scanner;
import java.util.Stack;
public class main {
   
    public static int isPossible(int[] pushed, int[] popped) {
        Stack<Integer> stack = new Stack<>();
        int i = 0;
        for (int num : pushed) {
            stack.push(num);
            while (!stack.isEmpty() && stack.peek() == popped[i]) {
                stack.pop();
                i++;
            }
        }
        return stack.isEmpty() ? 1 : 0;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the size of the arrays (n): ");
        int n = scanner.nextInt();
        
        int[] pushed = new int[n];
        int[] popped = new int[n];
        
        System.out.println("Enter the elements of pushed array:");
        for (int i = 0; i < n; i++) {
            pushed[i] = scanner.nextInt();
        }
        
        System.out.println("Enter the elements of popped array:");
        for (int i = 0; i < n; i++) {
            popped[i] = scanner.nextInt();
        }
        
        int result = isPossible(pushed, popped);
        System.out.println("Output: " + result);

        scanner.close();
    }
}

