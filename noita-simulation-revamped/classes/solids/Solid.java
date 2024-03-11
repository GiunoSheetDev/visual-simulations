package classes.solids;
import classes.Particle;

public class Solid extends Particle { 
    

    public Solid(int i, int j){
        super(i, j);
        
    }

    

    
    public Object[] getNeighbors(Object[][] tiles) {
        Object diagonalLeft = null;
        Object diagonalRight = null;
        Object[] returnList = new Object[2];

        if (this.j < tiles.length) {
            if (this.i == 0) {
                diagonalRight = tiles[this.i+1][this.j+1];
            }
            else if (this.i == tiles.length-1) {
                diagonalLeft = tiles[this.i-1][this.j+1];
            }
            else {// non sta sui bordi 
                diagonalRight = tiles[this.i+1][this.j+1];
                diagonalLeft = tiles[this.i-1][this.j+1];
            }
        }

        returnList[0] = diagonalLeft;
        returnList[1] = diagonalRight;

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
        
        return true;
    }
    
}
