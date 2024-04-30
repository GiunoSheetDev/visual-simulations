import java.util.Arrays;
import java.util.Random;
public class Body {
    
    private Random random = new Random();

    public double mass = 1.0e12;;
    public static final double G = -6.67430e-11;

    final int colorR = 255;
    final int colorB = 0;
    final int colorG = 0;

    public Vector2 position = new Vector2();
    public Vector2 velocity = new Vector2();
    public Vector2 acceleration = new Vector2();

    public Body(int posx, int posy) {
        this.position.vector = new double[] {posx, posy};
    }


    public static void main(String[] args) {
        Body b1 = new Body(1, 1);
        Body b2 = new Body(1, 4);
        Body b3 = new Body(5, 1);
        Body[] bodies = new Body[3];
        bodies[0] = b1;
        bodies[1] = b2;
        bodies[2] = b3;
        b1.feelGravity(bodies);
        b2.feelGravity(bodies);
        b3.feelGravity(bodies);
    }

    public void update() {
        this.position.add(this.velocity);
        this.velocity.add(this.acceleration);
        this.acceleration.vector = new double[2];
        
    }

    public void feelGravity(Body[] bodies) {
        Vector2 delta = new Vector2();
        int total = bodies.length;
        for (int i=0; i < total; i++) {
            Body b = bodies[i];
            if (b == this) continue;
            
            Vector2 currentPosition = new Vector2(this.position.x(), this.position.y());
            
            currentPosition.sub(b.position);
            
            double mag = currentPosition.mag();

            double denominatore = Math.pow(mag, 3);
            
            currentPosition.multByDouble(G);
            
            currentPosition.multByDouble(b.mass);
            
            currentPosition.divByDouble(denominatore);

            delta.sub(currentPosition);
            
        }
        
        this.acceleration.add(delta);
        
    }
}
