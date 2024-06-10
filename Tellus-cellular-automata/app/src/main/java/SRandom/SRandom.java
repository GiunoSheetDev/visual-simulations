package SRandom;

import java.util.Random;

// static random? seed random? idk something like that
public class SRandom {

    private static final Random RANDOM = new Random();
    private static int SEED;

    public static void setSeed(int seed) {
        RANDOM.setSeed(seed);
        SEED = seed;
    }

    public static int getSeed() {
        return SEED;
    }

    public static int nextInt(int n) {
        return RANDOM.nextInt(n);
    }

    // random int between min and max
    public static int randInt(int min, int max) {
        return RANDOM.nextInt(max - 1 - min) + min;
    }

    public static float nextFloat() {
        return RANDOM.nextFloat();
    }
    public static float nextFloat(int n) {
        return RANDOM.nextFloat(n);
    }

}
