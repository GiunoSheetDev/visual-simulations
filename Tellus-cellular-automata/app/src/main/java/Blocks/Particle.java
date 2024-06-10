package Blocks;

import SRandom.SRandom;

import Grid.Grid;

public abstract class Particle implements Cloneable {
    
    // to be abstracted by the solids
    // they are readonly
    private int colorRed;
    private int colorGreen;
    private int colorBlue;

    public float spawnRate = 1f;

    public int[] currentPosition = new int[] {-1, -1};
    public int[] previousPosition = new int[] {-1, -1}; // used to calculate isFreeFalling by seeing if moved last frame
    public boolean isFreeFalling;

    // isFreeFalling for gases, if they can still go up
    public boolean isRising;

    // when creating an object, if this particle is in the way it will not spawn the object removing this item (if false)
    public boolean canBeOverridden;

    public int scanDirection = 1; // NOTE: 1 bottom to top, 2 top to bottom

    // set top true when moved, set to false after rendering by the Window, to avoid calling on it update() more than once a frame
    public boolean hasMoved;
    // TODO: check when setting has moved if needing to change even particle that was moved

    //for fire and related stuff
    public boolean isFlammable; 
    public int fireLifetime = 200; //time until burning element turns into smoke
    public float chanceToSpreadFire = 0.02f;

    // TODO: 
    // public int fireResistance; // time needed to change from block to fire
    // public int burningFor; // how many ticks has been byurning, (before catching fire)

    public void setColors(int r, int g, int b) {
        this.colorRed = parseColor(r);
        this.colorGreen = parseColor(g);
        this.colorBlue = parseColor(b);
    }

    public int parseColor(int c) {
        // check if it is in bounds and in case return min or max values
        return Math.max(0, Math.min(c, 255));
    }

    public int getColorRed() {
        return colorRed;
    }

    public int getColorGreen() {
        return colorGreen;
    }

    public int getColorBlue() {
        return colorBlue;
    }

    // give random offset to add more texture to color
    public int getColorOffset() {
         //OFFSET IS += 100 quindi fare -50 da original rgb value
        return SRandom.nextInt(100);
    }

    public int[] getCurrentPosition() {
        return currentPosition;
    }
    
    // should be called at end of update function
    public void wakeUpAdjacentChunks(int [] coords, Grid grid) {
        if (coords[0] != previousPosition[0] || coords[1] != previousPosition[1])
            grid.wakeUpChunks(coords[0], coords[1]);
    }

    @Override
    public Particle clone() {
        try {
            return (Particle)super.clone();
        }
        catch (CloneNotSupportedException e) {
            e.printStackTrace();
            return null;
        }
    }


    public int[] update(int[] coords, Grid grid) {
        hasMoved = true;
        currentPosition = coords.clone();

        // NOTE: for water and other (if the particle doesnt update previous position)
        // i have no idea why it doesnt break anything but in case something breaks it probably for this
        //previousPosition = coords.clone();



        return coords;
    }

}
