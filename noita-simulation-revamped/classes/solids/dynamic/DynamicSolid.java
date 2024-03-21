package classes.solids.dynamic;
import classes.Particle;
import classes.liquids.Liquid;
import classes.solids.Solid;

import java.util.Arrays;
import java.util.Random;

public class DynamicSolid extends Solid{
    int dispersionRate;

    public DynamicSolid(int i, int j){
        super(i, j);
        this.dispersionRate = dispersionRate;
    }






    public Object[][] update(Object[][] tiles){
        try {
            Object bottom = tiles[this.i][this.j+1];
            int bottomI = this.i;
            int bottomJ = this.j+1;

            if (bottom instanceof Integer) {
                tiles = this.moveToEmptyCell(bottomI, bottomJ, tiles);
            }
            else if (bottom instanceof Liquid) {
                tiles = this.switchWithAnotherParticle(bottomI, bottomJ, tiles);
            }
            else if (bottom instanceof Solid) {
                Object[] neighbors = this.getNeighbors(tiles);
                Random r = new Random();
                int direction = r.nextInt(2);
                if (direction == 0){
                    if (this.canGoToCell(this.i-1, this.j+1, tiles)== true){
                        tiles = tryMovingToCell(tiles, this.i-1, this.j+1);
                    } else {
                        if (this.canGoToCell(this.i+1, this.j+1, tiles)== true){
                            tiles = tryMovingToCell(tiles, this.i+1, this.j+1);

                        }
                    }
                } else {
                    if (this.canGoToCell(this.i+1, this.j+1, tiles)== true){
                        tiles = tryMovingToCell(tiles, this.i+1, this.j+1);
                    } else {
                        if (this.canGoToCell(this.i-1, this.j+1, tiles)== true){
                            tiles = tryMovingToCell(tiles, this.i-1, this.j+1);

                        }
                    }
                }
                    

            }
                
            
            
            return tiles;

        }

        catch (Exception e) {
            
            
         }
        

        

        return tiles;
    }
}


            
