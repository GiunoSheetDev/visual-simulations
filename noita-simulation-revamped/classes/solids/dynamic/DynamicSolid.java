package classes.solids.dynamic;
import classes.Particle;
import classes.liquids.Liquid;
import classes.solids.Solid;
import java.util.Random;

public class DynamicSolid extends Solid{
    int dispersionRate;

    public DynamicSolid(int i, int j){
        super(i, j);
        this.dispersionRate = dispersionRate;
    }


    public Object[][] tryMovingToCell(Object[][] tiles, int targetI, int targetJ) {
        if (this.canGoToCell(targetI, targetJ, tiles)) {
            if (tiles[targetI][targetJ] instanceof Particle) {
                this.switchWithAnotherParticle(targetI, targetJ, tiles);
            } else {
                this.moveToEmptyCell(targetI, targetJ, tiles);
            }
            return tiles;
        }
        return null;
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
                System.out.println("BOTTOM IS SOLID");
            }

            
            
            return tiles;

        }








































            /* 
            Object bottom = tiles[this.i][this.j+1];
            System.out.println(bottom);
            

            if (bottom.equals(0)) { //if bottom is empty
                this.moveToEmptyCell(this.i, this.j+1, tiles);
            }

            else if (bottom instanceof Liquid) { //bottom is liquid
                this.switchWithAnotherParticle(this.i, this.j+1, tiles);
            }

            else if (bottom instanceof Solid) { //bottom is solid, check diagonals
                Object[] neighbors = this.getNeighbors(tiles);
                Object diagonalLeft = neighbors[0];
                Object diagonalRight = neighbors[1];
                
                Random random = new Random();
                int direction = random.nextInt(2);

                int diagonalLeftI = this.i-1;
                int diagonalLeftJ = this.j+1;
                int diagonalRightI = this.i+1;
                int diagonalRightJ = this.j+1;


                if (direction == 0) { // try to go left, in caso go right
                    Object[][] result = this.tryMovingToCell(diagonalLeft, tiles, diagonalLeftI, diagonalLeftJ);
                    if (result != null){}
                    else{
                        this.tryMovingToCell(diagonalRight, tiles, diagonalRightI, diagonalRightJ);
                    } 
                }
                else{
                    Object[][] result = this.tryMovingToCell(diagonalRight, tiles, diagonalRightI, diagonalRightJ);
                    if (result != null){}
                    else{
                        this.tryMovingToCell(diagonalLeft, tiles, diagonalLeftI, diagonalLeftJ);
                    } 
                }
            }

            
        }

            
        */
         catch (Exception e) {
            
            
         }
        

        

        return tiles;
    }
}


            
