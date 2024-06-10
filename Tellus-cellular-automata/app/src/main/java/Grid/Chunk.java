package Grid;

public class Chunk {
    public final int SIZE;

    private boolean shouldStep = true;
    private boolean shouldStepNextFrame = false;

    private int[] topLeft;

    public Chunk(int size) {
        SIZE = size;
    }

    // public void setTopLeft(int[] newTopLeft) {
    //     topLeft = newTopLeft;
    // }
    // public int[] getTopLeft() {
    //     return topLeft;
    // }

    public boolean getShouldStep() {
        return shouldStep;
    }
    public void setShouldStepNextFrame() {
        this.shouldStepNextFrame = true;
    }

    public void goToNextStep() {
        shouldStep = shouldStepNextFrame;
        shouldStepNextFrame = false;
    }
}
