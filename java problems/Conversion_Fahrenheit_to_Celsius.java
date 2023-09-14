/*Take the following as input.

Minimum Fahrenheit value
Maximum Fahrenheit value
Step

Print as output the Celsius conversions. Use the formula C = (5/9)(F – 32) E.g. for an input of 0, 100 and 20 the output is
0 -17
20 -6
40 4
60 15
80 26
100 37 */

import java.util.Scanner;

class Conversion_Fahrenheit_to_Celsius
{
    public static void main(String[] args)
    {
        // Scanner sc = new Scanner(System.in);
        // int minF = sc.nextInt();
        // int maxF = sc.nextInt();
        // int step = sc.nextInt();
        // int f = minF;
        // while(f <= maxF)
        // {
        //     int c = (int)((5.0/9)*(f-32));
        //     System.out.println(f + "\t" + c);
        //     f = f + step;
        // }
   Scanner sc=new Scanner(System.in);
         int min=sc.nextInt();
		 int max=sc.nextInt();
		 int step=sc.nextInt();
		 int c;
		 for(int i=min;i<=max;i=i+step)
		 {
			 c=(int)((5/9.0)*(i-32));
			 System.out.println(i+"\t"+c);
		 }
	}}
    

