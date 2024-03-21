import strategies.*;

public class Main {
    public static void main(String[] args) {
        
    }

    public Object[] runTournament() {
        //create an instance of every file in the folder "strategies"
        //let every strategy play against itself and against all others
        //the number of rounds is random. otherwise they would always defect (still around 200 tho)
        //save final result in an array ordered by number of points
        //all strategies have a method that reads the opponent previous move and either return True (cooperate) or False (defect) based on the logic of the strategy
        //Main has a method that lets strategies fight called runTournament
        

    }


    public static void singleFight(Strat strat1, Strat strat2) {
        previousStrat1 = null;
        previousStrat2 = null;
        
        sout(strat1.play(previousStrat2));
    
    
    }


}
