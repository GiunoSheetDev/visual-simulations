package Blocks.Solids.DynamicSolid;

public class Sand extends DynamicParticle {
    
    public Sand() {
        super();

        // make them shift a bit to create texture
        // original sand = 182, 155, 99
        int offset = getColorOffset();
        setColors(132 + offset, 105 + offset, 50 + offset);

        setMaxSpeed(5);
        setAcceleration(0.6f);

        setBehaviours(true, true, true);
    }
}
