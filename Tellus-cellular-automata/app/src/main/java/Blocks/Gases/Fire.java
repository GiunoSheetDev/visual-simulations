package Blocks.Gases;

import Blocks.Air;
import Blocks.Particle;
import Blocks.Liquids.LiquidParticle;
import Grid.Grid;
import SRandom.SRandom;

public class Fire extends GasParticle {
    
    int lifetime = SRandom.randInt(50, fireLifetime);
    int hasLivedFor = 0;
    boolean hasMovedLastFrame = false;
    
    
    int[][] availableColors = new int[][]{
        {255, 31, 31},
        {234, 90, 0}, 
        {255, 105, 0},
        {238, 204, 9},
        {240, 161, 65}
    };

    int currentColor = SRandom.nextInt(availableColors.length);



    public Fire() {
        super();

        setBehaviours(false, false, false, false, false);

        canBeOverridden = true;
        spawnRate = 0.2f;
    }



    public int[] update(int[] coords, Grid grid){
        super.update(coords, grid);

        //implemented like a Gas
        hasLivedFor++;
        if (hasLivedFor >= lifetime) {
            grid.setParticle(coords[0], coords[1], new Smoke());
            return coords;
        }

        hasMovedLastFrame = !hasMovedLastFrame;
        if (hasMovedLastFrame) return coords;

        currentColor = (currentColor + 1) % (availableColors.length -1);
        setColors(availableColors[currentColor][0] , availableColors[currentColor][1] , availableColors[currentColor][2] );

        for (Particle particle: grid.getNeighbors(coords[0], coords[1])) {
            if (particle == null || particle instanceof Air) return coords;

            // check if there is water (or liquid that doesnt catch fire) to eestinguish or there is a material to be flammable
            // TODO: with water fix it not estinguishing itself properly
            if (particle instanceof LiquidParticle && !particle.isFlammable) {
                grid.setParticle(coords[0], coords[1], new Smoke());
            }
            // spread to another particle if it is flammable (it substitutes any particle to fire) (to change method with oil)
            else if (particle.isFlammable && SRandom.nextFloat() <= chanceToSpreadFire) {
                int[] particlePos = particle.getCurrentPosition();
                grid.setParticle(particlePos[0], particlePos[1], new Fire());
            }
        }


        return coords;


    }
}
