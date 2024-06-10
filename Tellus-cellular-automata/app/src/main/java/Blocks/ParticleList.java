package Blocks;

import java.awt.Color;

import Blocks.Gases.Fire;
import Blocks.Gases.Smoke;
import Blocks.Liquids.Oil;
import Blocks.Liquids.Water;
import Blocks.Solids.DynamicSolid.Gravel;
import Blocks.Solids.DynamicSolid.Sand;
import Blocks.Solids.DynamicSolid.Snow;
import Blocks.Solids.StaticSolid.Stone;
import Blocks.Solids.StaticSolid.Wood;
;

// functions as big ass lookup table to get new instance of any particle

public class ParticleList {

    public static int numberOfParticleAvailable = 9; // TODO update every time we add a new particle VERY IMPORTANTO


    public static int getNumberOfParticleAvailable() {
        return numberOfParticleAvailable;
    }

    public Particle getNewParticle(int id) {
        

        switch (id) {
            case 0:
                return new Air();

            case 1:
                return new Sand();

            case 2:
                return new Snow();

            case 3:
                return new Wood();

            case 4:
                return new Water();

            case 5:
                return new Gravel();

            case 6:
                return new Oil();

            case 7:
                return new Smoke();

            case 8:
                return new Fire();

            case 9:
                return new Stone();
        }

        System.out.println("GET NEW PARTICLE PARTICLE WAS NOT INDEED FOUND");
        return new Air();
    }

    public Color getColorOfParticle(int id) {
        switch (id) {
            case 1:
                return new Color(182, 155, 99);

            case 2:
                return new Color(205, 205, 205);

            case 3:
                return new Color(83, 54, 43);

            case 4:
                return new Color(46, 82, 255);

            case 5:
                return new Color(158, 152, 134);

            case 6:
                return new Color(124, 130, 8);

            case 7:
                return new Color(79 , 78, 78);
            
            case 8:
                return new Color(189, 78, 31);

            case 9:
                return new Color(83, 84, 78);
        }

        System.out.println("COULD NOT FIND COLOR BOHO");
        return new Color(255, 255, 255);
   }
}
