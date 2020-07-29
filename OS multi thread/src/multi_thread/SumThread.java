package multi_thread;

public class SumThread implements Runnable {
    int sum = 0;
    @Override
    public void run() {
        for (int i = 0 ; i <= 100 ; i++) {
            sum = sum + i;
        }
    }
    
    public static void main(String args[]) {
        SumThread sum = new SumThread();
        Thread thread = new Thread(sum);
        thread.start();
        int result = sum.sum;
        System.out.println("Count result is:" + result);
    }
}