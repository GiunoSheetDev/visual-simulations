package classes;

public class Particle {
    public int i;
    public int j;

    //equivalent to def __init__
    public Particle(int i, int j){
        this.i = i;
        this.j = j;
    }

    public Object[][] moveToEmptyCell(int targetI, int targetJ, Object[][] tiles){
        tiles[targetI][targetJ] = this; // set self at target position
        tiles[this.i][this.j] = 0; // set current tile = 0
        this.i = targetI; //set self coords to target coords
        this.j = targetJ;
        
        return tiles;
    }

    public Object[][] switchWithAnotherParticle(int targetI, int targetJ, Object[][] tiles) {
        Particle target = (Particle) tiles[targetI][targetJ]; //get target instance
        tiles[this.i][this.j] = target; //set current tile = target
        tiles[targetI][targetJ] = this; //set self at target position
        
        target.i = this.i; //set target coords to current coords
        target.j = this.j; 

        this.i = targetI; // set self coords to target coords
        this.j = targetJ;

        return tiles;
    }

    

    
}
