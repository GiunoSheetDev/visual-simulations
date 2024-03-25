package strategies.TitForTatFamily;
import java.util.Random;

import strategies.Strat;

public class TitForTat implements Strat{
    private int points;

    public int getPoints() {
        return points;
    }

    public void setPoints(int points) {
        this.points = points;
    }


    public boolean play(Boolean oppMove) {
        if (oppMove == null) {
            return true;
        }
        else {
            return oppMove;
        }
    }
}
