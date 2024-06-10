package Blocks.Solids.StaticSolid;

import java.util.Random;

public class Wood extends StaticParticle {
    
    public Wood() {
        super();
        
        
        // make them shift a bit to create texture
        // original sand = 182, 155, 99
        int offset = getColorOffset();
        setColors(33 + offset, 4 + offset, -7 + offset);

        this.isFlammable = true;
    }
}
