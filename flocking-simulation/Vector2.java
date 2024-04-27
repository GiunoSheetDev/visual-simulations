//https://p5js.org/reference/#/p5.Vector

import java.util.Arrays;
import java.util.concurrent.ThreadLocalRandom;


public class Vector2 {
    public double[] vector = new double[2];
    public double x() { return vector[0];}
    public double y() { return vector[1];}

    public void print() {
        System.out.println(Arrays.toString(this.vector));
    }

    public void randomize(double minRange, double maxRange){
        this.vector[0] = ThreadLocalRandom.current().nextDouble(minRange, maxRange);
        this.vector[1] = ThreadLocalRandom.current().nextDouble(minRange, maxRange);
    }


    public void add(Vector2 v2) {
        this.vector[0] += v2.x();
        this.vector[1] += v2.y();
    }

    public void sub(Vector2 v2) {
        this.vector[0] -= v2.x();
        this.vector[1] -= v2.y();
    }

    public void mult(Vector2 v2) {
        this.vector[0] *= v2.x();
        this.vector[1] *= v2.y();
    }

    public void multByInt(int num) {
        this.vector[0] *= num;
        this.vector[1] *= num;
    }

    public void div(Vector2 v2) {
        this.vector[0] /= v2.x();
        this.vector[1] /= v2.y();
    }

    public void divByInt(int num) {
        this.vector[0] /= num;
        this.vector[1] /= num;
        
    }

    public void divByFloat(float num) {
        this.vector[0] /= num;
        this.vector[1] /= num;
        
    }



    public double mag() { return Math.sqrt(Math.pow(this.x(), 2) + Math.pow(this.y(), 2));} //pitagora 
    
    public void normalize() { //set len to 1
        double magnitude = this.mag();
        if (magnitude == 0) return;
        this.vector[0] /= magnitude;
        this.vector[1] /= magnitude;
    }

    public void setMag(double magnitude) { //https://stackoverflow.com/questions/41317291/setting-the-magnitude-of-a-2d-vector
        normalize();
        this.vector[0] *= magnitude;
        this.vector[1] *= magnitude;
    }

    public double heading() { 
        double toa = this.y() / this.x();
        double arctan = Math.atan(toa);
        if (this.x() >= 0 && this.y() >= 0) {
            return arctan;
        }
        else if (this.x() <= 0 && this.y() >= 0) {
            return 180-arctan;
        }
        else if (this.x() <= 0 && this.y() <= 0) {
            return 180+arctan;
        }
        else if (this.x() >= 0 && this.y() <= 0) {
            return 360-arctan;
        }
        return 0;
    }
    
    public void limit(double max) {
        double magnitude = this.mag();
        if (magnitude > max) {
            double ratio = max /magnitude;
            this.vector[0] *= ratio;
            this.vector[1] *= ratio;
        }
    }

}


