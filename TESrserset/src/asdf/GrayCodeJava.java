package asdf;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class GrayCodeJava {
    private int[] code;
    private boolean isOdd;
    public GrayCodeJava(int[] code, boolean isOdd) {
        this.code = code; 
        this.isOdd = isOdd;
    }
    
    public int lastIndexOf(int elem) {
        int i;
        for(i = code.length - 1; code[i] != elem; i--);
        return i;
    }
    
    public GrayCodeJava next() {
        int[] next = new int[0];
        int i = (isOdd ? code.length : lastIndexOf(1)) - 1;
        if(i != -1) {
            next = Arrays.copyOf(code, code.length);
            next[i] = 1 - next[i];
        }
        return new GrayCodeJava(next, !isOdd);
    }
    
    public boolean isEmpty() { return code.length == 0; }

    public String toString() {
        return Arrays.toString(code) + (isOdd ? " odd" : " even");
    }
    
    public static List<GrayCodeJava> gray(int length) {
        List<GrayCodeJava> grays = new ArrayList<>();
        GrayCodeJava gray = new GrayCodeJava(new int[length], true);
        do { grays.add(gray); } while(!(gray = gray.next()).isEmpty());
        return grays;
    }

    public static void main(String[] args) {
        for(GrayCodeJava gray : gray(4)) { System.out.println(gray); }
    }
}
