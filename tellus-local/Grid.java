import java.util.Arrays;
import java.util.concurrent.ThreadLocalRandom;

public class Grid {
    final int screenWidth;
    final int screenHeight;

    private final int rows;
    private final int columns;
    public int[][] grid = {{0}};
    

    public Grid(int screenWidth, int screenHeight, int tileDimension){
        this.screenWidth = screenWidth;
        this.screenHeight = screenHeight;
        this.rows = screenHeight / tileDimension;
        this.columns = screenWidth / tileDimension;
        grid = new int[this.rows][this.columns];
    }

    public static void main(String[] args) {
        Grid grid = new Grid(800, 800, 20);
        grid.generateRandomizedGrid();
        System.out.println(Arrays.toString(grid.grid[0]));
        grid.print();
    }

    public void generateEmptyGrid(){
        /*generates a 2d array of all zeros (id of empty cell)
        this is the general structure of the Grid
        WE NEED TO ITERATE FROM  BOTTOM TO TOP (L2R OR R2L DOESNT CHANGE ANYTHING)
        for (int j = columns-1; j > -1; j--) {
            for (int i = rows-1; i >-1; i--) where
        
        [^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ 
         0 0 0 0 0 0 0 0 0 0 0  |
         0 0 0 0 0 0 0 0 0 0 0  |
         0 0 0 0 0 0 0 0 0 0 0  | j
         0 0 0 0 0 0 0 0 0 0 0  |
         0 0 0 0 0 0 0 0 0 0 0  v
         v v v v v v v v v v v] 
        
            ------------> 
                  i

        */
        
        for (int i = 0; i < this.columns; i++){
            int[] row = new int[this.columns];
            for (int j = 0; j < this.rows; j++){
                row[j] = 0;
            }
            grid[i] = row;
        }
    }

    public void generateRandomizedGrid(){ 
        /*mostly for debugging purposes
        generates a random 2d array of numbers between 0 and 255
        */
        for (int i = 0; i < this.columns; i++){
            int[] row = new int[this.columns];
            for (int j = 0; j < this.rows; j++){
                row[j] = ThreadLocalRandom.current().nextInt(255);
            }
            grid[i] = row;
        }
    }

    public void print() {
        for (int[] row : grid) {
            System.out.println(Arrays.toString(row));
        }
    }




    
}
