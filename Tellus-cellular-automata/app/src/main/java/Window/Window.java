package Window;
//gradlew build && gradlew run  I'm lazy XD

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.SwingUtilities;
import javax.swing.Timer;

import Blocks.Particle;
import Blocks.ParticleList;
import Grid.Grid;


public class Window extends JPanel implements ActionListener {
    
    final int screenWidth;
    final int screenHeight;
    final int chunkSize;
    final int sidebarWidth;
    final int tileDimension;
    final int rows;
    final int columns;

    int FPS;
    int DELAY;
    Timer timer;

    // if not rendering in time for timer wait that first is done rendering and skip frame
    private boolean currentlyRendering;

    private static Grid grid;
    private boolean toDrawChunks;
    private boolean restart;

    private Mouse mouse = new Mouse();

    private boolean windowShouldClose = false; // set when hit esc to quit

    public ParticleList particleList = new ParticleList();
    public int currentSelectedParticle = 1;
    public Color currentSelectedParticleColor = particleList.getColorOfParticle(currentSelectedParticle);

    public int currentlySelectedTemplate = 0;


    

    public Window(int screenWidth, int screenHeight,int chunkSize, int sidebarWidth, int tileDimension, int fps) {
        this.screenWidth = screenWidth;
        this.screenHeight = screenHeight;
        this.chunkSize = chunkSize;
        this.sidebarWidth = sidebarWidth;
        this.tileDimension = tileDimension;
        this.rows = screenHeight / tileDimension;
        this.columns = screenWidth / tileDimension;

        this.FPS = fps;
        this.DELAY = 1000 / FPS;


        this.setPreferredSize(new Dimension(screenWidth + sidebarWidth, screenHeight));
        this.setBackground(Color.black); //dunno if its actually even useful since we color also the empty cell with a black square
        this.setDoubleBuffered(true); //improves performance

        this.setFocusable(true); //for using keyAdapter
        this.requestFocusInWindow();
        
        this.addKeyListener(new MyKeyAdapter());

        this.addMouseWheelListener(mouse);// for mouse wheel detection, changes cursour radius
        this.addMouseMotionListener(mouse);
        this.addMouseListener(mouse);

    }

    

    public void start() {
        restart = false;
        if (timer == null) { // keep same timer even if restarted
            timer = new Timer(DELAY, this);
            timer.setRepeats(true);
            timer.start();
        }

        grid = new Grid(screenWidth, screenHeight, chunkSize, tileDimension);
        

    }
    
    public void stop() {
        JFrame ancestor = (JFrame) SwingUtilities.getAncestorOfClass(JFrame.class, this);
        ancestor.dispose();
        System.exit(0);
    }

    public boolean getWindowShouldClose() {
        return windowShouldClose;
    }

    // NOTE: MAIN LOOP
    //called every timer clock cycle
    public void actionPerformed(ActionEvent event){
        if (currentlyRendering) return;
        currentlyRendering = true;

        //equivalent to pygame.display.update()
        //updates screen every clock cycle
        if (restart) start();
        if (getWindowShouldClose()) stop();


        grid.updateGrid();

        if (mouse.isDragged() || mouse.isPressed()) {
            setOnClick(); // set particle on the position of the mouse, when clicked
        };

        //setEntities();

        repaint(); // calls paintComponent
    
        // make particle moved be able to move again
        grid.setGridHasMovedFalse();

        // remove unloaded particles
        System.gc();

        currentlyRendering = false;
    }

    //called by repaint in actionPerformed
    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2 = (Graphics2D)g; // 2d gives more access on geometry, coords, ...

        if (grid != null) {
            drawGrid(g2);
            if (toDrawChunks) drawChunks(g2);
        }

        drawMouse(g2);
        

        g2.dispose(); // frees up memory
    }

    public void setOnClick() {
        int x = mouse.getX();
        int y = mouse.getY();
        if ( 0 > x || x > screenWidth - 1 || 0 > y || y > screenHeight - 1 ) return; // check if out of bounds

        grid.setCursor(x, y, mouse.getRadius(), currentSelectedParticle);
    }


    // TODO: change method to go j, i (if needed tbh idk if it will give problems)
    public void drawGrid(Graphics2D g){        
        // grid is saved perpewndicular so it must be draw in opposite way
        for (int i = 0; i < rows; i++){
            for (int j = 0; j < columns; j++) {
                Particle curr = grid.getAtPosition(i + grid.getViewportOffsetY(), j + grid.getViewportOffsetX());
                int colorRed = curr.getColorRed();
                int colorGreen = curr.getColorGreen();
                int colorBlue = curr.getColorBlue();
                g.setColor(new Color(colorRed, colorGreen, colorBlue));
                g.fillRect(j*tileDimension, i*tileDimension, tileDimension, tileDimension);                
            }
        }
    }

    public void drawChunks(Graphics2D g) {
        g.setColor(new Color(255, 255, 255));

        for (int j = 1; j < grid.getChunkColumns(); j++) {
            g.drawLine(
                j * chunkSize * tileDimension,
                0,
                j * chunkSize * tileDimension,
                screenHeight * tileDimension
            );

        }

        for (int i = 1; i < grid.getChunkRows(); i++) {
            g.drawLine(
                0,
                i * chunkSize * tileDimension,
                screenWidth * tileDimension,
                i * chunkSize * tileDimension
            );

        }

        // draw active chunks
        for (int i = 0; i < grid.getChunkRows(); i++){
            for (int j = 0; j < grid.getChunkColumns(); j++) {
                if (grid.getChunks()[i][j].getShouldStep()) {
                    g.setColor(new Color(255, 0, 0, 60));
                    g.fillRect(
                        j * chunkSize * tileDimension,
                        i * chunkSize * tileDimension,
                        chunkSize * tileDimension,
                        chunkSize * tileDimension
                    );                
                }
            }
        }

    }

    // // converts from window's coordinate to snapped window to grid coordinates for drawing
    // private int snapToGrid(int coord) {
    //     // (pos / tiledimension) * tiledimension works 
    //     // because java rounds to int the one in brackets so then we can treat it as i or j of drawGrid()
    //     return (coord / tileDimension) * tileDimension;
    // }

    public void drawMouse(Graphics2D g) {
        //g.setColor(new Color(currentSelectedParticle.getColorRed(), currentSelectedParticle.getColorGreen(), currentSelectedParticle.getColorBlue()));

        g.setColor(currentSelectedParticleColor);
        
        /*
         int radiusInPixels = mouse.getRadius() * tileDimension;
         int centerX = mouse.getX() / tileDimension * tileDimension;
         int centerY = mouse.getY() / tileDimension * tileDimension;

         g.fillOval(centerX - radiusInPixels, centerY - radiusInPixels, radiusInPixels * 2, radiusInPixels * 2);
        */
        
        int radius = mouse.getRadius() * tileDimension;
        int circleCentreX = (mouse.getX() / tileDimension) * tileDimension;
        int circleCentreY = (mouse.getY() / tileDimension) * tileDimension;
        
        int c0 = (((circleCentreX + radius) / tileDimension) * tileDimension); //c0 stands for 0 degrees on the circumference
        int c180 = (((circleCentreX - radius) / tileDimension) * tileDimension); //c180 stands for 180 degrees on the circumference
        int c90 = (((circleCentreY + radius) / tileDimension) * tileDimension); //c90 stands for 90 degrees on the circumference
        int c270 = (((circleCentreY - radius) / tileDimension) * tileDimension); //c270 stands for 270 degrees on the circumference       
        
        //int radiusInTiles = radius / tileDimension;
        // Calculate the number of tiles the circle spans in both directions
        //int numTilesX = Math.abs(c180 - c0) / tileDimension;
        //int numTilesY = Math.abs(c270 - c90) / tileDimension;

        // Adjust the loop conditions based on the actual number of tiles the circle spans
        for (int x = c180; x <= c0; x += tileDimension) {
            for (int y = c270; y <= c90; y += tileDimension) {
                if (Math.sqrt((x - circleCentreX) * (x - circleCentreX) + (y - circleCentreY) * (y - circleCentreY)) <= radius) {
                    g.fillRect(x, y, tileDimension, tileDimension);
                }
            }
        }
    }



    


    private class MyKeyAdapter extends KeyAdapter {
        @Override
        public void keyPressed(KeyEvent e) {
            int key = e.getKeyCode();
            //System.out.println(key);
            switch (key) {
                //full list here https://stackoverflow.com/questions/15313469/java-keyboard-keycodes-list
                case 10: // enter
                    restart = true;
                    break;

                case 27: // esc
                    windowShouldClose = true;
                    break;

                // arrows up and down to increase / decrease cursor
                case 38:
                    mouse.incrementCursor();
                    break;
                case 40:
                    mouse.decrementCursor();
                    break;

                
                // TODO: add all in one check
                //keyboards input to switch currently selected particle
                case 49: //F1
                    currentSelectedParticle = 1;
                    break;
            
                case 50: //F2
                    currentSelectedParticle = 2;
                    break;
                
                case 51: //F3
                    currentSelectedParticle = 3;
                    break;
                
                case 52: //F4
                    currentSelectedParticle = 4;
                    break;
                
                case 53: // F5
                    currentSelectedParticle = 5;
                    break;

                case 54: // F6
                    currentSelectedParticle = 6;
                    break;

                case 55:
                    currentSelectedParticle = 7;
                    break;

                case 56:
                    currentSelectedParticle = 8;
                    break;

                case 57:
                    currentSelectedParticle = 9;
                    break;

                case 58:  // rightarrow
                    currentSelectedParticle = (currentSelectedParticle +1) % ParticleList.getNumberOfParticleAvailable();
            
                case 37:
                    currentSelectedParticle = (currentSelectedParticle -1);
                    if (currentSelectedParticle < 0) currentSelectedParticle = ParticleList.getNumberOfParticleAvailable();
                    
                case 96:// numPad 0 
                    grid.generateWorld();
                       

                case 77:
                    //GridTemplates.saveCurrentGrid(grid);
                    break;

                default:
                    break;
            }






            

            // get ovverriden every input, we dont care we are not yandere dev we can, gls amio
            currentSelectedParticleColor = particleList.getColorOfParticle(currentSelectedParticle);

        }

        @Override
        public void keyReleased(KeyEvent e){
            int key = e.getKeyCode();


            if (key == 67) // c
                toDrawChunks = !toDrawChunks;
            if (key == 80) // p
                grid.print();
        }

    }

}
