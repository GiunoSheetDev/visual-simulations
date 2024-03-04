

public class Factorial {
    public static void main(String[] args) {
        System.out.println(getFactorial(14));
        
    }
    
    public static int getFactorial(int num) {
        int fact = 1;
        for (int i = 1; i <= num; i++) {
            fact *= i;
        }
        return fact;
    }


}
