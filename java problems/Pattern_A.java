public class Pattern_A {
    public static void main(String[] args) {
        int rows = 5;
        for(int i=1; i<=rows; i++) {
            for(int j=0; j<=rows-i; j++)
                System.out.print(" ");
            for(int j=0; j<2 * i -1; j++)    
            {   
                if (j == 0 || j == 2 * i - 2 || i == rows)   
                    System.out.print("*");   
                else   
                    System.out.print(" ");
              
            }
            System.out.println();    
        }
    }
}
