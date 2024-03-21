import java.util.Arrays;
import classes.solids.*;
import classes.solids.dynamic.*;
import classes.liquids.*;


public class Test {
    public static void main(String[] args) {
        int screenH = 800;
        int screenW = 800;
        int tileDimension = 200;
        int rows = screenH / tileDimension;
        int columns = screenW / tileDimension;


         
        Object[][] tiles = Tiles.getEmptyTiles(screenW, screenH, tileDimension);
        

        

        Water testSolid = new Water(1, 3);
        Water testSolid1 = new Water(1, 1);
        tiles[1][3] = testSolid;
        tiles[1][1] = testSolid1;
        Water testSolid2 = new Water(0, 0);
        Water testSolid3 = new Water(2, 0);
        tiles[0][0] = testSolid2;
        tiles[2][0] = testSolid3;
        Water testSolid4 = new Water(1, 0);
        Water testSolid5 = new Water(3, 0);
        tiles[1][0] = testSolid4;
        tiles[3][0] = testSolid5;

        System.out.println(Arrays.deepToString(tiles));
        tiles = Tiles.updateTiles(rows, columns, tiles);
        System.out.println(Arrays.deepToString(tiles));
        tiles = Tiles.updateTiles(rows, columns, tiles);
        System.out.println(Arrays.deepToString(tiles));
   
        System.out.println(Arrays.deepToString(tiles));
        tiles = Tiles.updateTiles(rows, columns, tiles);
        System.out.println(Arrays.deepToString(tiles));
        tiles = Tiles.updateTiles(rows, columns, tiles);
        System.out.println(Arrays.deepToString(tiles));
             

        /* moveToEmptyCell works
         * switchWithAnotherCell works
         * canGoToCell works
         * tryMovingToCell works
         * getNeighbors works
         * DynamicSolid.update works
         * Tiles.update works
         *
         * ALL WORKS SO FAR
         * 
         * 
         * Water seems to be working (havent checked with interaction with Sand tho)
         * 
         * 
         * 
         */
    }
}
