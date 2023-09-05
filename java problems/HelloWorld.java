
import java.util.*;
class HelloWorld {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
         System.out.println("enter array");
        String s[]=sc.next().split("");
        sc.close();
        int a[]=new int[s.length];
         //System.out.println(a.length);
    for(int i=0;i<s.length;i++)
        a[i]=Integer.parseInt(s[i]);
    System.out.print("Integer array is [");    
    for(int i=0;i<a.length;i++)
         System.out.print(a[i]+ " ");
    System.out.println("]");
    }
}