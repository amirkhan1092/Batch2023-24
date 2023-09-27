import java.util.Scanner;

class Kartik_bhayya_string {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int k = sc.nextInt();
        sc.nextLine();
        String s = sc.nextLine();


        int count_a = 0;
        int count_b = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'a')
                count_a++;
            else
                count_b++;
        }

        int min_count = Math.min(count_a, count_b);
        int max_count = Math.max(count_a, count_b);
        if(min_count >= k)
            System.out.println(max_count + k);
        else
            System.out.println(min_count + max_count);
    }
}