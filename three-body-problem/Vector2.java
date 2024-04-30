//https://p5js.org/reference/#/p5.Vector

import java.util.Arrays;
import java.util.concurrent.ThreadLocalRandom;



public class Vector2 implements Cloneable{
    public double[] vector = new double[2];
    public double x() { return vector[0];}
    public double y() { return vector[1];}


    public Vector2(){}

    public Vector2(double x, double y) {
        vector[0] = x;
        vector[1] = y;
    }



    public void print() {
        System.out.println(Arrays.toString(this.vector));
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

    public void multByLong(long num){
        this.vector[0] *= num;
        this.vector[1] *= num;
    }

    public void multByDouble(double num){
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

    public void divByDouble(double num) {
        this.vector[0] /= num;
        this.vector[1] /= num;
        
    }

    public void divByFloat(float num) {
        this.vector[0] /= num;
        this.vector[1] /= num;
        
    }

    public double distanceFrom(Vector2 v2) {
        return Math.sqrt(Math.pow(this.x()-v2.x(), 2) + Math.pow(this.y()-v2.y(), 2));
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
    
}