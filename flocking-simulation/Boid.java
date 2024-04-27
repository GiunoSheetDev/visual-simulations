import java.util.Random;
import java.util.ArrayList;

import javafx.scene.shape.CubicCurve;


public class Boid {
    private Random random = new Random();

    final int colorR = random.nextInt(256);
    final int colorG = random.nextInt(256);
    final int colorB = random.nextInt(256);

    public Vector2 position = new Vector2();
    public Vector2 velocity = new Vector2();
    public Vector2 acceleration = new Vector2();


    private int maxVelocity = 5;
    private float perceptionRadius = 520;
    private double maxSteeringForce = 0.4;
    
    public Boid(int screen_width, int screen_height) {
        this.velocity.randomize(-maxVelocity, maxVelocity);
        this.position.vector = new double[]{random.nextInt(screen_width), random.nextInt(screen_height)};
    }


    public void update(int screen_width, int screen_height) {
        
        this.position.add(this.velocity);
        this.velocity.add(this.acceleration);
        if (this.position.x() > screen_width) {
            this.position.vector[0] = 0;
        }
        else if (this.position.x() < 0) {
            this.position.vector[0] = screen_width;
        }
        if (this.position.y() > screen_height) {
            this.position.vector[1] = 0;
        }
        else if (this.position.y() < 0) {
            this.position.vector[1] = screen_height;
        }

        
        this.acceleration.vector = new double[2];

    }
    

    public Boid[] getFlockMates(Boid[] boids) {
        ArrayList<Boid> tempFlock = new ArrayList<Boid>();
        int total = 0;
        for (int i = 0; i < boids.length; i++) {
            
            Boid currentBoid = boids[i];
            if (currentBoid == this) continue;
            
            float distanceSquared =  (float) Math.pow((this.position.x()- currentBoid.position.x()), 2) + (float) Math.pow((this.position.y() - currentBoid.position.y()), 2); 
            
            if (distanceSquared > perceptionRadius) continue; 
            
            tempFlock.add(currentBoid);
            total++;
        }
        Boid[] flockMates = tempFlock.toArray(new Boid[total]);
        return flockMates;
    }



    public void alignment(Boid[] flockmates){
        Vector2 average = new Vector2();
        int total = flockmates.length;
        for (int i= 0; i < total; i++){
            average.add(flockmates[i].velocity);
        }

        if (total > 0) { 
            average.divByInt(total); 
            average.setMag(this.maxVelocity);
            average.sub(this.velocity);
            average.limit(this.maxSteeringForce); //https://www.youtube.com/watch?v=mhjuuHl6qHM&t=735s

        }

        this.acceleration.add(average);
    }

    public void cohesion(Boid[] flockmates){
        Vector2 average = new Vector2();
        int total = flockmates.length;
        for (int i= 0; i < total; i++) {
            average.add(flockmates[i].position);
        }

        if (total > 0) {
            average.divByInt(total);
            average.sub(this.position);
            average.setMag(this.maxVelocity);
            average.sub(this.velocity);
            average.limit(this.maxSteeringForce);
        }
        
        this.acceleration.add(average);
    }

    public void separation(Boid[] flockmates){
        Vector2 average = new Vector2();
        int total = flockmates.length;
        for (int i = 0; i < total; i++) {
            Boid currentBoid = flockmates[i];
            Vector2 difference = new Vector2();
            difference.vector = this.position.vector.clone();
            difference.sub(currentBoid.position);
            float distanceSquared =  (float) Math.pow((this.position.x()- currentBoid.position.x()), 2) + (float) Math.pow((this.position.y() - currentBoid.position.y()), 2); //inversely proportional to the square, might change the final result
            if (distanceSquared != 0) { difference.divByFloat(distanceSquared);}

            average.add(difference);
        }

        if (total > 0) {
            average.divByInt(total);
            average.setMag(this.maxVelocity);
            average.sub(this.velocity);
            average.limit(this.maxSteeringForce);
        }
        
        this.acceleration.add(average);

    }
}
