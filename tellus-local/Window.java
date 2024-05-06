import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.util.Arrays;

import javax.swing.Timer;
import javax.xml.parsers.FactoryConfigurationError;
import javax.swing.JPanel;
import javax.swing.JFrame;


public class Window extends JPanel implements ActionListener {
    
    static final int screenWidth = 800;
    static final int screenHeight = 800;
    static final int tileDimension = 20;
    static final int rows = screenHeight / tileDimension;
    static final int columns = screenWidth / tileDimension;

    final int fps = 30;
    final int delay = 1000/fps;
    Timer timer;

    static Grid grid;
    boolean restart;

    Window() {
        this.setPreferredSize(new Dimension(screenWidth, screenHeight));
        this.setBackground(Color.black); //dunno if its actually even useful since we color also the empty cell with a black square
        this.setDoubleBuffered(true); //improves performance

        this.setFocusable(true); //for using keyAdapter
        this.requestFocusInWindow();
        this.addKeyListener(new MyKeyAdapter());
    }

    

    public void start() {
        restart = false;
        if (timer == null) {
            timer = new Timer(delay, this);
            timer.setRepeats(true);
            timer.start();
        }

        grid = new Grid(screenWidth, screenHeight, tileDimension);
        grid.generateRandomizedGrid();
    }

    public class MyKeyAdapter extends KeyAdapter {
        @Override
        public void keyPressed(KeyEvent e) {
            switch (e.getKeyCode()) {
                //full list here https://stackoverflow.com/questions/15313469/java-keyboard-keycodes-list
                case 10:
                    restart = true;
                    break;
            
                default:
                    break;
            }
        }
    }

    //called every timer clock cycle
    public void actionPerformed(ActionEvent event){
        //equivalent to pygame.display.update()
        if (restart) start();
        repaint();
    }

    //called by repaint in actionPerformed
    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2 = (Graphics2D)g; // 2d gives more access on geometry, coords, ...
        drawGrid(g2);
        g2.dispose(); // frees up memory
    }

    public void drawGrid(Graphics g){        
        for (int i = 0; i < rows; i++){
            for (int j = 0; j < columns; j++) {
                int color = grid.grid[i][j];
                g.setColor(new Color(color, color, color));
                g.fillRect(j*tileDimension, i*tileDimension, tileDimension, tileDimension);                
            }
        }
    }

    public static void main(String[] args) {
        JFrame screen = new JFrame();
        screen.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        screen.setResizable(false);
        screen.setTitle("rock-paper-scissors");

        Window window = new Window();
        screen.add(window);
        screen.pack(); // resize window to fit preferred size (specified in gamepanel)

        screen.setLocationRelativeTo(null); // specify location of the window // unll -> display at center of screen
        screen.setVisible(true); 

        window.start();
    }
   


    

    
}