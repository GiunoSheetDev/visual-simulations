package strategies.ProbabilisticFamily;

import java.util.Random;

import strategies.Strat;

public class ThreeQuarterRandomCooperation implements Strat{
    private int points;

    public int getPoints() {
        return points;
    }

    public void setPoints(int points) {
        this.points = points;
    }


    public boolean play(Boolean oppMove) {
        Random r = new Random();
        int decision = r.nextInt(4);
        if (decision == 2) {
            return false;
        }
        else {return true;}
    } 
}
