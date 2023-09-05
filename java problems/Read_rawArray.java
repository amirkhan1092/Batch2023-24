import java.util.Scanner;

class Read_rawArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter space separated integers: ");
        String[] str = sc.nextLine().split(" ");
        int[] arr = new int[str.length];
        for (int i = 0; i < str.length; i++) {
            arr[i] = Integer.parseInt(str[i]);
        }
        sc.close();
        for (int i : arr) {
            System.out.println(i);
        }
        
        
    }
}