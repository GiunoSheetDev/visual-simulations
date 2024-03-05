import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

public class Euler203 {
    public static void main(String[] args) {
        long numberOfRows = 8; // works up to a certain value then overflows
        long[][] tartaglia = getTartagliaTriangle(numberOfRows);
        System.out.println(Arrays.deepToString(tartaglia));
        System.out.println(squarefreeBinomialCoefficient(tartaglia));
    }

    public static long binomialCoefficient(long n, long k) {

        long factN = Factorial.getFactorial(n);
        long factK = Factorial.getFactorial(k);
        long denominator = factK * Factorial.getFactorial(n-k);

        return (factN / denominator);

    }

    public static long[][] getTartagliaTriangle(long numberOfRows) {
        long[][] finalArray = new long[(int) numberOfRows][];
        
        for (int i = 0; i < numberOfRows; i++){
            long[] tempArray = new long[(int)i+1];

            for (int j = 0; j <= i; j++){
                long binomialCoefficient = binomialCoefficient(i, j);
                tempArray[j] = binomialCoefficient;
            }
        
            finalArray[i] = tempArray;
        }

        return finalArray;
                  
    }

    public static List<Long> squarefreeBinomialCoefficient(long[][] array) {
        List<Long> squarefreeList = new ArrayList<>();

        long numberOfRows = array.length;
        for (int i = 0; i < numberOfRows; i++){
            double len = Math.ceil(array[i].length/2);
            long tempLen = (int) len;
            for (int j = 0; j < tempLen; j++) { //check if in the divisor list there is a square of prime
                boolean isSquareFree = false;
                List<Long> tempDivisors = Divisors.getDivisors(array[i][j]);
                List<Long> tempPrimes = Divisors.getPrimeNumbers(array[i][j]);
                


                for (int k = 0; k < tempPrimes.size(); k++){
                    long elementToCheck = tempPrimes.get(k);
                    double squareToCheck = Math.pow(elementToCheck, 2);
                    long numToCheck = (int) squareToCheck;
            

                    isSquareFree = tempDivisors.contains(numToCheck);
                    
                    if (isSquareFree == true) {
                        break;
                    }

            
                }

                if (isSquareFree == false) {
                    squarefreeList.add(array[i][j]);
                }
            }
        }
        return squarefreeList;


    }





}
