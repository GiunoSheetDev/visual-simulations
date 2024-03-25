import strategies.*;
import strategies.ProbabilisticFamily.PureDefection;
import strategies.ProbabilisticFamily.ThreeQuarterRandomCooperation;
import strategies.ProbabilisticFamily.ThreeQuarterRandomDefection;
import strategies.TitForTatFamily.*;


import java.util.Random;

public class Main {
    public static void main(String[] args) {
        Strat titfor2tat = new ThreeQuarterRandomDefection();
        Strat titfortat = new TitForTat();
        singleFight(titfor2tat, titfortat);
        System.out.println("titfor2tat " + titfor2tat.getPoints());
        System.out.println("titfortat " +titfortat.getPoints());
        
        
    }

    public Object[] runTournament() {
        //create an instance of every file in the folder "strategies"
        //let every strategy play against itself and against all others
        //the number of rounds is random. otherwise they would always defect (still around 200 tho)
        //save final result in an array ordered by number of points
        //all strategies have a method that reads the opponent previous move and either return True (cooperate) or False (defect) based on the logic of the strategy
        //Main has a method that lets strategies fight called runTournament
        Object[] temp = new Object[0];
        return temp;

    }
 

    public static void singleFight(Strat strat1, Strat strat2) {
        Boolean previousMoveStrat1 = null;
        Boolean previousMoveStrat2 = null;
        for (int i = 0; i < 200; i++){
            boolean currentMoveStrat1 = strat1.play(previousMoveStrat2);
            boolean currentMoveStrat2 = strat2.play(previousMoveStrat1);
            
            System.out.println(currentMoveStrat1 +  " " + strat1.getPoints());
            System.out.println(currentMoveStrat2 +  " " + strat2.getPoints());

            if (currentMoveStrat1 == true && currentMoveStrat2 == true) {
                strat1.setPoints(strat1.getPoints()+3);
                strat2.setPoints(strat2.getPoints()+3);
            }
            else if (currentMoveStrat1 == false && currentMoveStrat2 == true){
                strat1.setPoints(strat1.getPoints()+5);
            }
            else if (currentMoveStrat1 == true && currentMoveStrat2 == false){
                strat2.setPoints(strat2.getPoints()+5);
            }
            else {
                strat1.setPoints(strat1.getPoints()+1);
                strat2.setPoints(strat2.getPoints()+1);
            }
            
            previousMoveStrat1 = currentMoveStrat1;
            previousMoveStrat2 = currentMoveStrat2;


            
        }
        
        
        
        
    
    
    }


}
