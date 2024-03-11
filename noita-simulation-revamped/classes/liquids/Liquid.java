package classes.liquids;
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
    
        if (0 < this.i && this.i < (tiles.length-1)) {
            diagonalLeft = tiles[this.i-1][this.j+1];
            diagonalRight = tiles[this.i+1][this.j+1];
            left = tiles[this.i-1][this.j];
            right = tiles[this.i+1][this.j];
        }
        else if (this.i == 0) {
            diagonalRight = tiles[this.i+1][this.j+1];
            right = tiles[this.i+1][this.j];
        }
        else if (this.i == (tiles.length-1)) {
            diagonalLeft = tiles[this.i-1][this.j+1];
            left = tiles[this.i-1][this.j];
        }
        returnList[0] = diagonalLeft;
        returnList[1] = diagonalRight;
        returnList[2] = left;
        returnList[3] = right;

        return returnList;
    
    }


    public boolean canGoToCell(Object cell) {
        if (cell == null) {
            return false;
        }
        else if (cell instanceof Solid) {
            return false;
        }
        else if (cell instanceof Liquid) {
            Liquid liquidCell = (Liquid) cell;
            if (this.density > liquidCell.density) {
                return true;
            }
            else {
                return false;
            }
        }

        return true;

    }


    
}
