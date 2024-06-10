package Window;

import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.MouseMotionAdapter;
import java.awt.event.MouseWheelEvent;
import java.awt.event.MouseWheelListener;

public class Mouse extends MouseMotionAdapter implements MouseListener, MouseWheelListener{
    private int x;
    private int y;

    private int radius = 1; // draw area around mouse
    private int maxRadius = 20;
    private int minRadius = 0;

    private boolean pressed, dragged; // starts with false by default
    private int wheel; // amount of scrolling

    public void mouseMoved(MouseEvent e) {
        // divide by tile size to get what position in grid mouse is currently hovering onto
        updateMousePosition(e);
        // System.out.println("Mouse x: " + x + " y: " + y);
    }

    public void incrementCursor() {
        radius = Math.min(radius + 1, maxRadius);
    }
    public void decrementCursor() {
        radius = Math.max(radius - 1, minRadius);
    }

    @Override
    public void mouseDragged(MouseEvent e) {
        // This method is called when the mouse is moved while a button is pressed
        updateMousePosition(e);
        dragged = true;
        //System.out.println("Dragged");
    }

    public void updateMousePosition(MouseEvent e) {
        x = e.getX();
        y = e.getY();
    }

    @Override
    public void mouseClicked(MouseEvent e) {
        // NOTE: useless so far
        //System.out.println("Click");
    }

    @Override
    public void mousePressed(MouseEvent e) {
        pressed = true;
        //System.out.println("Pressed");
    }

    @Override
    public void mouseReleased(MouseEvent e) {
        dragged = pressed = false;
        //System.out.println("Released");
    }

    @Override
    public void mouseEntered(MouseEvent e) {
        // TODO: Auto-generated method stub
        //System.out.println("Entered");
    }

    @Override
    public void mouseExited(MouseEvent e) {
        dragged = pressed = false;
        //System.out.println("Exited");
    }


    public int getX() {
        return x;
    }
    public int getY() {
        return y;
    }

    public int getRadius() {
        return radius;
    }
    public void setRadius(int radius) {
        this.radius = radius;
    }

    public boolean isPressed() {
        return pressed;
    }
    public boolean isDragged() {
        return dragged;
    }


    @Override
    public void mouseWheelMoved(MouseWheelEvent e) {
        // detects the rotation of the wheel (inverted so scrolling toward oneself == -1)

        wheel = - e.getWheelRotation();
        radius = Math.min(radius + wheel, maxRadius);
        radius = Math.max(radius + wheel, minRadius);
        
    }

    public int getWheel() {
        return wheel;
    }
    
    

}
