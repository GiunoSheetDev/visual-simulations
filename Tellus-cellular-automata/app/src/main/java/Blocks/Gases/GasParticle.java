package Blocks.Gases;

import Blocks.Air;
import Blocks.Particle;
import Blocks.Solids.SolidParticle;
import Grid.Grid;

import SRandom.SRandom;

public abstract class GasParticle extends Particle {

    boolean hasMovedLastFrame;

    // for how many frames it will live for
    int lifetime = SRandom.randInt(200, 300);
    int hasLivedFor = 0; // how many frames particle has been alive for in respect of lifetime

    // behaviours
    private boolean goUp = true;
    private boolean goUpLeft = true;
    private boolean goUpRight = true;
    private boolean moveLeft = true;
    private boolean moveRight = true;


    public GasParticle() {
        super();

        isRising = true;
        scanDirection = 2; // top to bottom

        canBeOverridden = true;

        // spawnRate = 0.03f;
        spawnRate = 0.01f;
    }

    public void setLifetime(int lifetime) {
        this.lifetime = lifetime;
    }

    public void setBehaviours(boolean goUp, boolean goUpLeft, boolean goUpRight, boolean moveLeft, boolean moveRight) {
        this.goUp = goUp;
        this.goUpLeft = goUpLeft;
        this.goUpRight = goUpRight;
        this.moveLeft = moveLeft;
        this.moveRight = moveRight;
    }

    @Override
    public int[] update(int[] coords, Grid grid) {
        super.update(coords, grid);

        // always wake this chunk up
        grid.wakeUpChunks(coords[0], coords[1]);

        hasLivedFor++;
        // has lived a fulfilling life and now needs to go
        if (hasLivedFor >= lifetime) {
            grid.setParticle(coords[0], coords[1], new Air());
            return coords;
        }

        hasMovedLastFrame = !hasMovedLastFrame;
        if (hasMovedLastFrame) return coords;

        // change color to more dark the more it has lived
        setColors(
            this.getColorRed()  - 1,
            this.getColorGreen() - 1,
            this.getColorBlue() - 1
        );

        // TODO: add in grid second pass to update from top to bottom

        Particle[] upper = grid.getUpperNeighbors(coords[0], coords[1]);
        if (upper[1] == null) {
            isRising = false;
            return coords;
        }

        isRising = upper[1] instanceof Air || upper[1].isRising
            || !(coords[0] == previousPosition[0] && coords[1] == previousPosition[1]);
        if (isRising) previousPosition = coords.clone();

        // if block upper is not a solid swap with block upper
        if (goUp && isRising && upper[1] != null && !(upper[1] instanceof SolidParticle || upper[1] instanceof GasParticle)) {
            grid.setParticle(coords[0], coords[1], grid.getAtPosition(coords[0] - 1, coords[1]));
            grid.setParticle(coords[0] - 1, coords[1], this);
            coords[0]--;
        }

        // go to block to left if is not solid
        else if (goUpLeft && upper[0] != null && !(upper[0] instanceof SolidParticle || upper[0] instanceof GasParticle)) {
            grid.setParticle(coords[0], coords[1], grid.getAtPosition(coords[0] - 1, coords[1] - 1));
            grid.setParticle(coords[0] - 1, coords[1] - 1, this);
            coords[0]--;
            coords[1]--;
        }

        // go to block to right if is not solid
        else if (goUpRight && upper[2] != null && !(upper[2] instanceof SolidParticle || upper[2] instanceof GasParticle)) {
            grid.setParticle(coords[0], coords[1], grid.getAtPosition(coords[0] - 1, coords[1] + 1));
            grid.setParticle(coords[0] - 1, coords[1] + 1, this);
            coords[0]--;
            coords[1]++;
        }

        Particle[] side = grid.getSideNeighbors(coords[0], coords[1]);

        if (moveLeft && side[0] != null && SRandom.nextInt(2) == 0 && !(side[0] instanceof SolidParticle || side[0] instanceof GasParticle)) {
            grid.setParticle(coords[0], coords[1], grid.getAtPosition(coords[0], coords[1] - 1));
            grid.setParticle(coords[0], coords[1] - 1, this);
            coords[1]--;
        }
        else if (moveRight && side[1] != null && !(side[1] instanceof SolidParticle || side[1] instanceof GasParticle)) {
            grid.setParticle(coords[0], coords[1], grid.getAtPosition(coords[0], coords[1] + 1));
            grid.setParticle(coords[0], coords[1] + 1, this);
            coords[1]++;
        }

        return coords;
    }

}
