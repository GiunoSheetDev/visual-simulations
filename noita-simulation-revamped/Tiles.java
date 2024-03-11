import java.util.Arrays;

import classes.Particle;
import classes.solids.Solid;
import classes.solids.dynamic.DynamicSolid;

public class Tiles {
    public static void main(String[] args) {
        int screenH = 800;
        int screenW = 800;
        int tileDimension = 200;
        int rows = screenH / tileDimension;
        int columns = screenW / tileDimension;


        
        
        
        
        
    }

    public static Object[][] getEmptyTiles(int screenW, int screenH, int tileDimension) {
        int rows = screenH / tileDimension;
        int columns = screenW / tileDimension;
        
        Object[][] tiles = new Object[rows][columns];

        for (int i = 0; i < columns; i++ ){
            Object[] row = new Object[columns];
            for (int j = 0; j < rows; j++ ){
                row[j] = 0;
            }

            tiles[i] = row;
        }

        return tiles;

    }

    
    public static Object[][] updateTiles(int rows, int columns, Object[][] tiles) {
        for (int j = columns-1; j > -1; j--) {
            for (int i = rows-1; i >-1; i--){
                Object currentTile = tiles[i][j];
                if (currentTile instanceof DynamicSolid) {
                    DynamicSolid solidTile = (DynamicSolid) currentTile;
                    solidTile.update(tiles);
                }
            }
        }
        
        return tiles;
    }


    


    
}
