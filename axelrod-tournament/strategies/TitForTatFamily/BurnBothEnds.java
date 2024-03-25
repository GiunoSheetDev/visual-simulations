package strategies.TitForTatFamily;

import strategies.Strat;
import java.util.Random;

public class BurnBothEnds implements Strat{
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
        else if (oppMove == false) {
            Random r = new Random();
            int decision = r.nextInt(10);
            if (decision == 6) {
                return false;
            }
            
        }
        return oppMove;
    }
    
}
