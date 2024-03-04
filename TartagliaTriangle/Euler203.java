import java.util.Arrays;
import java.math.BigInteger; 

public class Euler203 {
    public static void main(String[] args) {
        int numberOfRows = 20; // works up to a certain value then overflows
        int[][] tartaglia = getTartagliaTriangle(numberOfRows);
        System.out.println(Arrays.deepToString(tartaglia));
       
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





}
