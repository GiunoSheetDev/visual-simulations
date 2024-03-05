import java.util.ArrayList;
import java.util.List;

public class Divisors {
    public static void main(String[] args) {
        System.out.println(getDivisors(4));
        System.out.println(getPrimeNumbers(4));
    }

    public static List<Integer> getDivisors(int num) {
        List<Integer> divisors = new ArrayList<>();
        for (int i = 1; i <= Math.sqrt(num); i++) {
            if (num % i == 0){
                divisors.add(i);
                if (i != num/i) { //avoid duplicate perfect square
                    divisors.add(num/i);

                }
            }
        }
        return divisors;
    }


    public static List<Integer> getPrimeNumbers(int N) {
        List<Integer> primes = new ArrayList<>();
        for (int x = 2; x <= N; x++) {
            boolean isPrime = true;
            for (int y = 2; y <= x / 2; ++y) {
                if (x % y == 0) {
                    isPrime = false;
                    break;
                }
            }
            if (isPrime) {
                primes.add(x);
            }
        }
        return primes;
    }



    
}
