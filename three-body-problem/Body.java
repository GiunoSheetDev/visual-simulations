import java.util.Arrays;
import java.util.Random;
public class Body {
   
    private Random random = new Random();

    public double mass = 1.0e13;
    public static final double G = 6.67430e-10;


    final int colorR;
    final int colorB;
    final int colorG;

    public Vector2 position = new Vector2();
    public Vector2 velocity = new Vector2();
    public Vector2 acceleration = new Vector2();

    private static final double SOFTENING_FACTOR = 1e5;



    public Body(int posx, int posy, int colorR, int colorG, int colorB) {
        this.position.vector = new double[] {posx, posy};
        this.colorR = colorR;
        this.colorG = colorG;
        this.colorB = colorB;
    }


    public static void main(String[] args) {
        Body b1 = new Body(1, 1, 255, 0, 0);
        Body b2 = new Body(1, 4, 0, 255, 0);
        Body b3 = new Body(5, 1, 0, 0, 255);
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
            double deltax = b.position.x() - this.position.x();
            double deltay = b.position.y() - this.position.y();
            double distanceSquared = (deltax*deltax + deltay*deltay) + SOFTENING_FACTOR;
            double force = G * this.mass * b.mass / (distanceSquared);
            double angle = Math.atan2(deltay, deltax);
            delta.vector[0] += force * Math.cos(angle) / this.mass;
            delta.vector[1] += force * Math.sin(angle) / this.mass;
            
            
        }
        
        this.acceleration.add(delta);
        
    }
}
