package Blocks.Solids.StaticSolid;

import java.util.Random;

public class Stone extends StaticParticle {
    
    public Stone() {
        super();
        
        


        int offset = getColorOffset();
        setColors(33 + offset, 34 + offset, 28 + offset);
    }
}
