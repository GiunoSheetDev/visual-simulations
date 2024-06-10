package Blocks.Liquids;

import Blocks.Air;
import Blocks.Particle;
import Blocks.Gases.GasParticle;
import Blocks.Solids.SolidParticle;
import Grid.Grid;
import SRandom.SRandom;



public abstract class LiquidParticle extends Particle {

    private int maxSpeed = 0; // how many cells to move ain one frame
    private float acceleration = 0; // 32bits, will never need more
    private float velocity = 0;
    // private boolean isOnGround = false;
    private int density = 0;
    private int dispersionRate = 2;

    public LiquidParticle() {
        super();

        canBeOverridden = true;
        spawnRate = 0.5f;
    }

    public void setMaxSpeed(int max) {
        maxSpeed = max;
    }

    public void setAcceleration(float accel) {
        acceleration = accel;
    }

    public void setDensity(int dens) {
        density = dens;
    }

    public int getDensity() {
        return density;
    }

    public void resetVelocity() {
        velocity = 0;
    }

    public float getVelocity() {
        return velocity;
    }

    public void updateVelocity() {
        velocity = Math.min(velocity + acceleration, maxSpeed);
    }

    @Override
    public int[] update(int[] coords, Grid grid) {
        super.update(coords, grid);

        previousPosition = coords.clone();

        updateVelocity();

        for (int n = 0; n <= velocity; n++) {

            Particle[] under = grid.getLowerNeighbors(coords[0], coords[1]);


            // move down
            if (under[1] != null && !(under[1] instanceof SolidParticle || under[1] instanceof LiquidParticle) ) {
                Particle toMove = grid.getAtPosition(coords[0] + 1, coords[1]);
                // remove gas particles
                if (toMove instanceof GasParticle)
                    grid.setParticle(coords[0], coords[1], new Air());
                else
                    grid.setParticle(coords[0], coords[1], toMove);

                grid.setParticle(coords[0] + 1, coords[1], this);
                coords[0]++;
            }


            // move sideways if there is no solid or liquid (will have to add a way to mix liquid but for now its good)
            // if liquid doesnt move it doesnt wake the chunk unnecessarily

            float random = SRandom.nextFloat(); // go to same direction multiple times in a row
            for (int i = 0; i <=  dispersionRate; i++) {
                Particle[] side = grid.getSideNeighbors(coords[0], coords[1]);
                if (side[0] != null && (random > 0.5f) && !(side[0] instanceof SolidParticle || side[0] instanceof LiquidParticle)) {
                    grid.setParticle(coords[0], coords[1], grid.getAtPosition(coords[0], coords[1] - 1));
                    grid.setParticle(coords[0], coords[1] - 1, this);
                    coords[1]--;
                }
                else if (side[1] != null && !(side[1] instanceof SolidParticle || side[1] instanceof LiquidParticle)) {
                    grid.setParticle(coords[0], coords[1], grid.getAtPosition(coords[0], coords[1] + 1));
                    grid.setParticle(coords[0], coords[1] + 1, this);
                    coords[1]++;
                }
            }

        }

        wakeUpAdjacentChunks(coords, grid);


        return coords;

    }

    
}
