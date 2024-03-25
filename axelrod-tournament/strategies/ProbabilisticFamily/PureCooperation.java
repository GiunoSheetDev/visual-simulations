package strategies.ProbabilisticFamily;

import java.util.Random;

import strategies.Strat;

public class PureCooperation implements Strat{
    private int points;

    public int getPoints() {
        return points;
    }

    public void setPoints(int points) {
        this.points = points;
    }


    public boolean play(Boolean oppMove) {
        return true;
    }
}
