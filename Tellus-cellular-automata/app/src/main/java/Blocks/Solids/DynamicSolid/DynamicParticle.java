package Blocks.Solids.DynamicSolid;

import Blocks.Air;
import Blocks.Gases.GasParticle;
import Blocks.Liquids.LiquidParticle;
import Blocks.Particle;
import Blocks.Solids.SolidParticle;

import Grid.Grid;
//import MusicPlayer.MusicPlayer;



abstract class DynamicParticle extends SolidParticle {

    private int maxSpeed = 0; // how many cells to move ain one frame
    private float acceleration = 0; // 32bits, will never need more
    private float velocity = 0;
    private float horizontalVelocity = 0;

    // behaviours
    private boolean goDown;
    private boolean goDownLeft;
    private boolean goDownRight;


    public DynamicParticle() {
        super();
    }

    public void setBehaviours(boolean goDown, boolean goDownLeft, boolean goDownRight) {
        this.goDown = goDown;
        this.goDownLeft = goDownLeft;
        this.goDownRight = goDownRight;
    }

    public void setMaxSpeed(int max) {
        maxSpeed = max;
    }

    public void setAcceleration(float accel) {
        acceleration = accel;
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

    // NOTE: coords -> j, i passed by reference
    @Override
    public int[] update(int[] coords, Grid grid) {
        super.update(coords, grid);

        updateVelocity();
        float currentVel = velocity;

        for (int n = 0; n <= velocity; n++) {

            Particle[] under = grid.getLowerNeighbors(coords[0], coords[1]);
            if (under[1] == null) {
                isFreeFalling = false;
                resetVelocity();

                return coords; // cannot move or you finish out of bounds
            }

            // if has air beneath or moved since last frame
            isFreeFalling = under[1] instanceof Air || under[1].isFreeFalling || !(coords[0] == previousPosition[0] && coords[1] == previousPosition[1]);
            if (isFreeFalling) previousPosition = coords.clone();

            // NOTE: it always swaps with the cell it goes to
            // make smoke disappear (if it is gas it creates air and doesnt make the gas rise)

            if (!isFreeFalling || under[1] instanceof LiquidParticle) { // sabbia quando entra in acqua non ha più gravità e cade lentamente
                horizontalVelocity = velocity;
                resetVelocity(); 
            }

            // if block under is not a solid nor an entity swap with block under
            if (goDown && !(under[1] instanceof SolidParticle)) {
                Particle particleBelow = grid.getAtPosition(coords[0] + 1, coords[1]);

                // if particle below is a gas make it air, else swap blocks
                grid.setParticle(coords[0], coords[1], particleBelow instanceof GasParticle? new Air() : particleBelow);
                grid.setParticle(coords[0] + 1, coords[1], this);
                coords[0]++;
            }

            // go to block to left if is not solid nor entity
            else if (goDownLeft && under[0] != null && !(under[0] instanceof SolidParticle)) {
                grid.setParticle(coords[0], coords[1], grid.getAtPosition(coords[0] + 1, coords[1] - 1));
                grid.setParticle(coords[0] + 1, coords[1] - 1, this);
                coords[0]++;
                coords[1]--;
            }

            // go to block to right if is not solid nor entity
            else if (goDownRight && under[2] != null && !(under[2] instanceof SolidParticle)) {
                grid.setParticle(coords[0], coords[1], grid.getAtPosition(coords[0] + 1, coords[1] + 1));
                grid.setParticle(coords[0] + 1, coords[1] + 1, this);
                coords[0]++;
                coords[1]++;
            }

            wakeUpAdjacentChunks(coords, grid);

            // TODO: fix to merge with check to wake up chunks or remove if not needed
            // updated version for check in other specific classes
            isFreeFalling = under[1] instanceof Air || under[1].isFreeFalling || !(coords[0] == previousPosition[0] && coords[1] == previousPosition[1]);
            if (isFreeFalling) {
                previousPosition = coords.clone();
                velocity = currentVel;
            };


        }

        return coords;

    }
}
