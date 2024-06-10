package Blocks;

import Grid.Grid;

public class Air extends Particle {

    public Air() {
        canBeOverridden = true;
    }

    // does not need to be updated
    @Override
    public int[] update(int[] coords, Grid grid) {
        return coords;
    }

}
