package strategies.TitForTatFamily;
import strategies.*;

public class TitFor2Tats implements Strat{
    private int points;
    private Boolean[] moveArray;
    private int turn;

    public TitFor2Tats() {
        this.moveArray = new Boolean[200];
        this.turn = 0;
        
    }

    public int getPoints() {
        return points;
    }

    public void setPoints(int points) {
        this.points = points;
    }


    public boolean play(Boolean oppMove) {
        if (oppMove == null) {
            oppMove = true; // Default to true if opponent's move is null
        }
        
        this.moveArray[this.turn] = oppMove;

        if (this.turn < 2) {
            // Cooperate on the first two turns
            this.turn++;
            return true;
        }

        if (oppMove == false) {
            if (this.moveArray[this.turn-2] == false) {
                // If the opponent defected twice in a row, defect for the next two turns
                this.turn++;
                return false;
            }
        }

        // Otherwise, mimic the opponent's last move
        this.turn++;
        return oppMove;
    }
}
