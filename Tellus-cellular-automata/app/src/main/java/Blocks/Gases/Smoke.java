package Blocks.Gases;

import Blocks.Air;
import Blocks.Particle;
import Grid.Grid;
import SRandom.SRandom;

public class Smoke extends GasParticle  {

    public Smoke() {
        super();

        int offset = getColorOffset();
        setColors(30 + offset, 38 + offset, 38 + offset);
    }

    @Override
    public int[] update(int[] coords, Grid grid) {
        super.update(coords, grid);

        // if upper neighbor is flammable make it become fire
        for (Particle particle: grid.getUpperNeighbors(coords[0], coords[1])) {
            if (particle == null || particle instanceof Air) return coords;

            if (particle.isFlammable && SRandom.nextFloat() <= chanceToSpreadFire / 3000) {
                int[] particlePos = particle.getCurrentPosition();
                grid.setParticle(particlePos[0], particlePos[1], new Fire());
            }
        }

        return coords;
    }

    
}
