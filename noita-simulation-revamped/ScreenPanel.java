import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Arrays;
import javax.swing.Timer;
import javax.swing.JPanel;


public class ScreenPanel extends JPanel implements ActionListener{
    
    static final int screenW = 800;
    static final int screenH = 800;
    static final int tileDimension = 5;

    static final int columns = screenW / tileDimension;
    static final int rows = screenH / tileDimension;

    final int fps = 30;
    final int delay = 1000 / fps;
    Timer timer;

    Object[][] tiles = Tiles.getEmptyTiles(screenW, screenH, tileDimension);
    
    public static void main(String[] args) {
        System.out.println("res: " + screenW + "(height) x " + screenH + "(width)");
    }

    ScreenPanel() {
        this.setPreferredSize(new Dimension(screenW, screenH));
        this.setBackground(Color.black);
        this.setDoubleBuffered(true);
    }



    
}
