package Blocks.Liquids;

public class Water extends LiquidParticle{
    static public int maxSpeed = 10;
    
    public Water() {
        super();

        // make them shift a bit to create texture
        // int offset = getColorOffset();
        // setColors(-4 + offset, 32 + offset, 205 + offset);
        setColors(46, 82, 255);

        setMaxSpeed(maxSpeed);
        setAcceleration(1.6f);

    }
}
