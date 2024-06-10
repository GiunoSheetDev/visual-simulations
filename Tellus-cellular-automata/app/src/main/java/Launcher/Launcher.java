package Launcher;

import javax.swing.JFrame;

// import MusicPlayer.MusicPlayer;
import SRandom.SRandom;
import Window.Window;

public class Launcher {
    static private JFrame screen;
    static private Window window;

    static final int SEED = 42; // TODO: all random is determined with this seed
    

    // NOTE: leave them different to debug
    static final int TILE_SIZE = 5;
    static final int CHUNK_SIZE = 32;
    static final int WIDTH = CHUNK_SIZE * TILE_SIZE * 8; // 1.280
    static final int HEIGHT = CHUNK_SIZE * TILE_SIZE * 6; // 960
    static final int SIDEBAR_WIDTH = 0; //(int)(WIDTH * .3);

    static int FPS = 30;

    public static void main(String[] args) {
        SRandom.setSeed(SEED);
        // System.out.println("seed: " + SRandom.getSeed());

        screen = new JFrame();
        screen.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        screen.setResizable(false);
        screen.setTitle("Tellus");

        window = new Window(WIDTH, HEIGHT, CHUNK_SIZE, SIDEBAR_WIDTH, TILE_SIZE, FPS);
        screen.add(window);
        screen.pack(); // resize window to fit preferred size (specified in gamepanel)

        screen.setLocationRelativeTo(null); // specify location of the window // null -> display at center of screen
        screen.setVisible(true); 
        
        // MusicPlayer player = new MusicPlayer();
        // player.playFile("src/main/assets/audio/blocks/landed.wav");

        window.start();

    }

}
