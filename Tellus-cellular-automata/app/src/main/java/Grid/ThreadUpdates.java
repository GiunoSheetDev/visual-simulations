package Grid;

import java.util.concurrent.CountDownLatch;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

import Blocks.Air;

public class ThreadUpdates {

    private final int nThreads = Runtime.getRuntime().availableProcessors() - 1; // how many unused cores the pc has
    private final ExecutorService es;

    private final int screenColumns;
    private final int chunkSize; // how many pixels to update horizontally for one thread

    private CountDownLatch latch;

    public ThreadUpdates(int screenColumns) {
        this.screenColumns = screenColumns;
        this.chunkSize = screenColumns / nThreads;
        es = Executors.newFixedThreadPool(nThreads);
        // System.out.println("number of threads: " + nThreads);
    }

    public void update(Grid grid) {
        latch = new CountDownLatch(nThreads / 2); // nthreads

        es.execute(() -> {
            // even threads
            for (int threadN = 0; threadN < nThreads; threadN += 2) {
                // first pass
                for (int j = grid.getRows() - 1; j > -1; j--) {
                    for (int i = chunkSize; i > -1; i--) {
                        //System.out.println(i + " " + threadN);
                        int offsetI = i + chunkSize * threadN;
                        if (grid.grid[j][offsetI] instanceof Air || grid.grid[j][offsetI].scanDirection != 1 || grid.grid[j][offsetI].hasMoved) continue;

                        grid.grid[j][offsetI].update(new int[]{j, offsetI}, grid);
                    }
                }
                latch.countDown();
            }

        });


        waitTillDone();

        latch = new CountDownLatch(nThreads / 2);

        es.execute(() -> {
            // odd threads
            for (int threadN = 1; threadN < nThreads; threadN += 2) {
                // first pass
                for (int j = grid.getRows() - 1; j > -1; j--) {
                    for (int i = chunkSize; i > -1; i--) {
                        //System.out.println(i + " " + threadN);
                        int offsetI = i + chunkSize * threadN;
                        if (grid.grid[j][offsetI] instanceof Air || grid.grid[j][offsetI].scanDirection != 1 || grid.grid[j][offsetI].hasMoved) continue;

                        grid.grid[j][offsetI].update(new int[]{j, offsetI}, grid);
                    }
                }
                latch.countDown();
            }
        });

        waitTillDone();
    }

    public void waitTillDone() {
        // es.shutdown(); // do not accept any new tasks
        try {
            latch.await();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            // Handle interruption
        }


    }

}

// individual thread to run update
// from bottom to up
class FirstPassThread implements Runnable {

    @Override
    public void run() {

    }

}
