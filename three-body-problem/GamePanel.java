import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.awt.geom.AffineTransform;
import java.awt.geom.Line2D;
import java.awt.image.BufferedImage;
import java.util.Arrays;

import javax.swing.Timer;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class GamePanel extends JPanel implements ActionListener {

    static final int SCREEN_WIDTH = 1600;
    static final int SCREEN_HEIGHT = 800;

    final int FPS = 30;
    final int DELAY = 1000 / FPS;
    Timer timer;

    boolean restart;

    final int BODIES_NUMBER = 3;
    Body[] planets = new Body[BODIES_NUMBER];

    private BufferedImage canvas;
    private JLabel label;
    

    public GamePanel() {
        this.setPreferredSize(new Dimension(SCREEN_WIDTH, SCREEN_HEIGHT)); // set window size
        this.setBackground(Color.black);
        this.setDoubleBuffered(true); // all drawing from this component will be done in an offscreen painting buffer -> improves performance

        this.setFocusable(true); // to use keyAdapter
        this.requestFocusInWindow();
        this.addKeyListener(new MyKeyAdapter());

        canvas = new BufferedImage(SCREEN_WIDTH, SCREEN_HEIGHT, BufferedImage.TYPE_INT_ARGB);
        label = new JLabel(new ImageIcon(canvas));
        this.add(label);

        System.out.println("ready.");
    }

    public void start() {
        restart = false;

        System.out.println("game loop running, fps: " + FPS);
        if (timer == null) {
            timer = new Timer(DELAY, this);
            timer.setRepeats(true);
            timer.start();
        }

        // populate boid array
        Body b1 = new Body(600, 400, 255, 0, 0);
        Body b2 = new Body(900, 500, 0, 255, 0);
        Body b3 = new Body(750, 250, 0, 0, 255);

        planets[0] = b1;
        planets[1] = b2;
        planets[2] = b3;
    }

    public class MyKeyAdapter extends KeyAdapter {
        @Override
        public void keyPressed(KeyEvent e) {
            switch (e.getKeyCode()) {
                case 32:
                    // if space pressed
                    restart = true;
                    System.out.print("restarted: ");
                    break;

                default:
                    break;
            }
        }
    }

    // called when the timer ends
    public void actionPerformed(ActionEvent event) {
        if (restart) start();
    
        // Move all boids of the flock
        for (Body b : planets) {
            b.feelGravity(planets);
            b.update();
        }
    
        // Update the canvas with the new positions
        Graphics2D g2 = canvas.createGraphics();
        g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
        for (Body b : planets) {
            g2.setColor(new Color(b.colorR, b.colorG, b.colorB));
            g2.fillOval((int) b.position.x() - 5, (int) b.position.y() - 5, 10, 10); // Draw the planet at its current position

        }
        g2.dispose();
        label.repaint(); // Trigger a repaint of the JLabel to reflect the updated canvas
    }
}