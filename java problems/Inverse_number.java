
/*Take the following as input.
A number
Assume that for a number of n digits, the value of each digit is from 1 to n and is unique. E.g. 32145 is a valid input number.

Write a function that returns its inverse, where inverse is defined as follows

Inverse of 32145 is 12543. In 32145, “5” is at 1st place, therefore in 12543, “1” is at 5th place; in 32145, “4” is at 2nd place, therefore in 12543, “2” is at 4th place.

Print the value returned. */

import java.util.Scanner;

public class Inverse_number {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String n = sc.nextLine();
        int[] arr = new int[n.length()];
        for(int i = 0; i < n.length(); i++)
        {
            arr[i] = Integer.parseInt(n.substring(i, i+1));
        }
        int[] inv = new int[arr.length];
        for(int i = 0; i < arr.length; i++)
        {
            inv[arr[i]-1] = i+1;
        }
        for(int i = 0; i < inv.length; i++)
        {
            System.out.print(inv[i]);
        }

        

        
    }
}
