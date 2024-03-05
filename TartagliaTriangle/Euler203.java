import java.util.Arrays;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;

public class Euler203 {
    public static void main(String[] args) {
        int numberOfRows = 8; // works up to a certain value then overflows
        int[][] tartaglia = getTartagliaTriangle(numberOfRows);
        System.out.println(Arrays.deepToString(tartaglia));
        System.out.println(squarefreeBinomialCoefficient(tartaglia));
    }

    public static int binomialCoefficient(int n, int k) {

        int factN = Factorial.getFactorial(n);
        int factK = Factorial.getFactorial(k);

        
        int denominator = factK * Factorial.getFactorial(n-k);

        return (factN / denominator);

    }

    public static int[][] getTartagliaTriangle(int numberOfRows) {
        int[][] finalArray = new int[numberOfRows][];
        
        for (int i = 0; i < numberOfRows; i++){
            int[] tempArray = new int[i+1];

            for (int j = 0; j <= i; j++){
                int binomialCoefficient = binomialCoefficient(i, j);
                tempArray[j] = binomialCoefficient;
            }
        
            finalArray[i] = tempArray;
        }

        return finalArray;
                  
    }

    public static List<Integer> squarefreeBinomialCoefficient(int[][] array) {
        List<Integer> squarefreeList = new ArrayList<>();

        int numberOfRows = array.length;
        for (int i = 0; i < numberOfRows; i++){
            double len = Math.ceil(array[i].length/2);
            int tempLen = (int) len;
            for (int j = 0; j < tempLen; j++) { //check if in the divisor list there is a square of prime
                boolean isSquareFree = false;
                List<Integer> tempDivisors = Divisors.getDivisors(array[i][j]);
                List<Integer> tempPrimes = Divisors.getPrimeNumbers(array[i][j]);


                for (int k = 0; k < tempPrimes.size(); k++){
                    int elementToCheck = tempPrimes.get(k);
                    double squareToCheck = Math.pow(elementToCheck, 2);
                    int numToCheck = (int) squareToCheck;

                    isSquareFree = tempDivisors.contains(numToCheck);

            
                }

                if (isSquareFree == false) {
                    squarefreeList.add(array[i][j]);
                }

                /*for (int k = 0; k < tempPrimes.size(); k++) {
                    elementToCheck = tempPrimes.get(k);
                    (int) squareToCheck = Math.pow(elementToCheck, 2);
                    isSquareFree = tempDivisors.contains(squareToCheck);

                    if (isSquareFree == true) {
                        squarefreeList.add(array[i][j]);
                        break;
                    }


                }
                */

            }
        }
        return squarefreeList;


    }





}
