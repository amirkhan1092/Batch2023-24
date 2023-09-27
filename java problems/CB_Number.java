import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static boolean intersection(int val1, int val2) {
        return Integer.toString(val1).contains(Integer.toString(val2)) || Integer.toString(val2).contains(Integer.toString(val1));
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int ndigit = scanner.nextInt();
        String digits = scanner.next();
        List<Integer> lst = new ArrayList<>();
        lst.add(2);
        lst.add(3);
        lst.add(5);
        lst.add(7);
        lst.add(11);
        lst.add(13);
        lst.add(17);
        lst.add(19);
        lst.add(23);
        List<Integer> out_lst = new ArrayList<>();

        for (int i = 0; i < digits.length(); i++) {
            for (int j = i; j < digits.length(); j++) {
                int num = Integer.parseInt(digits.substring(i, j + 1));
                if (lst.contains(num) || (num != 0 && num != 1) && (lst.stream().allMatch(d -> num % d != 0))) {
                    boolean foundIntersection = false;
                    for (int dt : out_lst) {
                        if (intersection(num, dt)) {
                            foundIntersection = true;
                            break;
                        }
                    }
                    if (!foundIntersection) {
                        out_lst.add(num);
                    }
                }
            }
        }

        System.out.println(out_lst.size());
    }
}
