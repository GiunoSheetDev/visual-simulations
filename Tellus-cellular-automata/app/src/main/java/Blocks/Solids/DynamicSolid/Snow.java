package Blocks.Solids.DynamicSolid;

import java.util.Arrays;

import Blocks.Particle;
import Blocks.Liquids.Water;
import Grid.Grid;
import Blocks.Liquids.LiquidParticle;


public class Snow extends DynamicParticle {
    public boolean hasMovedLastFrame; //way to make it go slower than 1 fps
    private int counterUntilMelts; 

    public Snow() {
        super();

        this.counterUntilMelts = 0;
        // make them shift a bit to create texture
        int offset = getColorOffset(); // change luminosity
        setColors(155 + offset, 155 + offset, 155 + offset);

        setMaxSpeed(1);
        setAcceleration(0);

        setBehaviours(true, true, true);

        spawnRate = 0.01f;

    }

    @Override
    public int[] update(int[] coords, Grid grid) {

        // move once every two frames
        if (!hasMovedLastFrame) super.update(coords, grid);
        hasMovedLastFrame = !hasMovedLastFrame;


        //check if the any neighbor particle is Liquid
        Particle[] neighbors = grid.getNeighbors(coords[0], coords[1]); 
        int counter = 0;
        for (int i = 0; i < neighbors.length - 1; i++) {
            if (neighbors[i] instanceof LiquidParticle) counter++;
        }

        if (counter == 0) this.counterUntilMelts = 0;
        else this.counterUntilMelts ++;

        if (this.counterUntilMelts == 180){ //number is arbitrary can be changed later on
            grid.setParticle(coords[0], coords[1], new Water());
        }

        return coords;
    }
}
