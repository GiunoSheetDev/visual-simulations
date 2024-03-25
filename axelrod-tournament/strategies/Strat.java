package strategies;

public interface Strat {
    
    boolean play(Boolean oppMove);
    int getPoints();
    void setPoints(int points);
}
