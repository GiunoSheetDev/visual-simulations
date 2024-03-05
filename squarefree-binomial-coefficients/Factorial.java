

public class Factorial {
    public static void main(String[] args) {
        System.out.println(getFactorial(51));
        
    }
    
    public static long getFactorial(long num) {
        long fact = 1;
        for (long i = 1; i <= num; i++) {
            fact *= i;
        }
        return fact;
    }


}
