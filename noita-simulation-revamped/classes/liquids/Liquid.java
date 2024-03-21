package classes.liquids;
import java.util.Random;

import classes.Particle;
import classes.solids.Solid;


public class Liquid extends Particle {
    public int density;

    public Liquid(int i, int j) {
        super(i, j);
    }


    public Object[] getNeighbors(Object[][] tiles) {
        Object diagonalLeft = null;
        Object diagonalRight = null;
        Object left = null;
        Object right = null;
        Object[] returnList = new Object[4];
    
        if (this.j < tiles.length){
            if (this.i == 0) {
                diagonalRight = tiles[this.i+1][this.j+1];
                right = tiles[this.i+1][this.j];
            }
            else if (this.i == tiles.length-1) {
                diagonalLeft = tiles[this.i-1][this.j+1];
                left = tiles[this.i-1][this.j];
            }
            else {
                diagonalRight = tiles[this.i+1][this.j+1];
                right = tiles[this.i+1][this.j];
                diagonalLeft = tiles[this.i-1][this.j+1];
                left = tiles[this.i-1][this.j];
            }
        }


        returnList[0] = diagonalLeft;
        returnList[1] = diagonalRight;
        returnList[2] = left;
        returnList[3] = right;

        return returnList;
    
    }
 

    public boolean canGoToCell(int targetI, int targetJ, Object[][] tiles) {
        Object cell = tiles[targetI][targetJ];
        if (cell == null) {
            return false;
        }
        else if (cell instanceof Solid) {
            return false;
        }
        else if (cell instanceof Liquid) {
            Liquid liquidCell = (Liquid) cell;
            if (this.density >= liquidCell.density) {
                return false;
            }
            return true; // if this.density is lower than the target they switch
        }

        return true;

    }

    public Object[][] tryMovingDiagonally(Object[][] tiles) {
        Object[] neighbors = this.getNeighbors(tiles);
        Random r = new Random();
        int direction = r.nextInt(2);
        
        
        

        if (direction == 0) { //try going diagonalLeft
            int diagonalLeftI = this.i-1;
            int diagonalLeftJ = this.j+1;
            if (this.canGoToCell(diagonalLeftI, diagonalLeftJ, tiles) == true) {
                tiles = tryMovingToCell(tiles, diagonalLeftI, diagonalLeftJ);
            }
            else { // diagonalLeft failed, try diagonalRight
                int diagonalRightI = this.i+1;
                int diagonalRightJ = this.j+1;
                if (this.canGoToCell(diagonalRightI, diagonalRightJ, tiles) == true) {
                    tiles = tryMovingToCell(tiles, diagonalRightI, diagonalRightJ);
                }
                else { //diagonalLeft failed, diagonalRight failed, try left
                    int leftI = this.i-1;

                    if (this.canGoToCell(leftI, this.j, tiles) == true) {
                        tiles = tryMovingToCell(tiles, leftI, this.j);
                    }
                    else { //diagonalLeft failed, diagonalRight failed, left failed, try right
                        int rightI = this.i+1;
                        if (this.canGoToCell(rightI, this.j, tiles) == true) {
                            tiles = tryMovingToCell(tiles, rightI, this.j);
                        }
                    }
                }
            }
        } 
        else { //try going diagonalRight
            int diagonalRightI = this.i+1;
            int diagonalRightJ = this.j+1;
            if (this.canGoToCell(diagonalRightI, diagonalRightJ, tiles) == true) {
                tiles = tryMovingToCell(tiles, diagonalRightI, diagonalRightJ);
            }
            else { // diagonalLeft failed, try diagonalRight
                int diagonalLeftI = this.i-1;
                int diagonalLeftJ = this.j+1;
                if (this.canGoToCell(diagonalLeftI, diagonalLeftJ, tiles) == true) {
                    tiles = tryMovingToCell(tiles, diagonalLeftI, diagonalLeftJ);
                }
                else { //diagonalLeft failed, diagonalRight failed, try left
                    int leftI = this.i-1;

                    if (this.canGoToCell(leftI, this.j, tiles) == true) {
                        tiles = tryMovingToCell(tiles, leftI, this.j);
                    }
                    else { //diagonalLeft failed, diagonalRight failed, left failed, try right
                        int rightI = this.i+1;
                        if (this.canGoToCell(rightI, this.j, tiles) == true) {
                            tiles = tryMovingToCell(tiles, rightI, this.j);
                        }
                    }
                }
            }
        }

        return tiles;
    }



    public Object[][] update(Object[][] tiles) {
        try {
            Object bottom = tiles[this.i][this.j+1];
            int bottomI = this.i;
            int bottomJ = this.j+1;
            
            if (bottom instanceof Integer) {
                tiles = this.moveToEmptyCell(bottomI, bottomJ, tiles);
                System.out.println(this + " BOTTOM IS EMPTY " + bottom);
            }
            else if (bottom instanceof Liquid) {
                if (this.canGoToCell(bottomI, bottomJ, tiles) == true) {
                    tiles = this.switchWithAnotherParticle(bottomI, bottomJ, tiles);
                    System.out.println(this + " BOTTOM IS LIQUID BUT CAN GO "+ bottom);
                    
                }
                else {
                    tiles = this.tryMovingDiagonally(tiles);
                    System.out.println(this + " BOTTOM IS LIQUID AND CANT GO "+ bottom);
                    
                }
            }

            else if (bottom instanceof Solid) {
                tiles = this.tryMovingDiagonally(tiles);
                
            }
        }
        catch (Exception e) {
            System.out.println("ERRORE " + this + " " + e);

        }

        return tiles;

    }


    
}
