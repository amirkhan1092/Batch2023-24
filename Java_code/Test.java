

// java Exception 
// java.lang.Exception


/**
 * Test
 */
public class Test {
    public int add(int a, int b) throws IndexOutOfBoundsException {
        int [] arr = new int[5];
        arr[6] = 1;
        return a / b;
    }
     public static void main(String[] args) {
            try {
                Test t = new Test();
                // throw new IndexOutOfBoundsException("My Exception");
                 int a = 10;
                 int b = 0;
                 int c = t.add(a, b);
                 System.out.println(c);
            } catch (ArithmeticException e) {
                 System.out.println("Error: " + e.getMessage());
            }
            finally{
                 System.out.println("Finally block");
            }
     }
}