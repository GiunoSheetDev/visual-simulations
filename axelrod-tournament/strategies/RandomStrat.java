package strategies;
import java.util.Random;

public class RandomStrat implements Strat{

    public int points;

    public static void main(String[] args) {
       
    }

    public boolean play(Boolean oppMove) {
        Random r = new Random();
        boolean myMove = r.nextBoolean();
        return myMove;
    }
}
