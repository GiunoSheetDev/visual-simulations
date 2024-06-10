package Blocks.Solids.DynamicSolid;


import Blocks.Air;
import Blocks.Particle;
import Grid.Grid;

public class Gravel extends DynamicParticle {
    boolean movedAfterLanding = false;
    
    public Gravel() {
        super();

        // make them shift a bit to create texture
        int offset = getColorOffset();
        setColors(108 + offset, 102 + offset, 84 + offset);

        setMaxSpeed(5);
        setAcceleration(0.6f);

        setBehaviours(true, false, false);
    }

    @Override
    public int[] update(int[] coords, Grid grid) {
        // run generic dynamic solid update

        super.update(coords, grid);

        if (isFreeFalling) {
            movedAfterLanding = false;
            return coords;
        }

        if (movedAfterLanding) return coords;

        // we landed for the first time and have to move
        movedAfterLanding = true;

        // TODO: make them work  here and not in dynamic solid
        // additional gravel updates
        // MOVE ONCE AFTER LANDING
        

        //Particle under = grid.getLowerNeighbors(coords[0], coords[1])[1];
        //if (under instanceof Air || under instanceof Gravel) return coords;

        //doesnt freefall diagonally
        // if (this instanceof Gravel) {
        //     

        Particle[] side = grid.getSideNeighbors(coords[0], coords[1]);


        if (side[0] != null && side[0] instanceof Air) {
            grid.setParticle(coords[0], coords[1], grid.getAtPosition(coords[0], coords[1]-1));
            grid.setParticle(coords[0], coords[1] - 1 , this);
            return coords;
        }

        else if (side[1] != null && side[1] instanceof Air) {
            grid.setParticle(coords[0], coords[1], grid.getAtPosition(coords[0], coords[1] + 1));
            grid.setParticle(coords[0], coords[1] + 1 , this);
            return coords;
        }
        // }

        return coords;
    }
}
