package Blocks.Solids.StaticSolid;

import Blocks.Particle;
import Blocks.Solids.SolidParticle;
import Grid.Grid;



abstract class StaticParticle extends SolidParticle {

    private int maxSpeed = 0; // how many cells to move ain one frame
    private float acceleration = 0; // 32bits, will never need more
    private float velocity = 0;
    
    public StaticParticle() {
        super();
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

    @Override
    public int[] update(int[] coords, Grid grid) {
        super.update(coords, grid);
        return coords;
    }


    

    
}
