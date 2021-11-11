import java.util.Scanner;
import java.lang.Math;
import java.io.*;

public class FileWriting {
/*
    public class Useful {
        public static void main(String[] args) {
            System.out.println("\n\tNobody:\n\tJava:");
            int bigest = Integer.MAX_VALUE;
            System.out.println("\t" + bigest + " + 1 = " + (bigest + 1) + "\n");
        }
        public static String reverse(String reversee) {
            // init a result to add each letter to
            String result = "";
            // loop backwards through the string and concat the letter to result
            for (int i = reversee.length() - 1; i >= 0; i--) {
                result += reversee.substring(i, i+1);
            }
            // return result
            return result;
        }
        public static Scanner newScanner() {
            return new Scanner(System.in);
        }
        public static int howMany(String s, char chr) {
            int count = 0;
            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i) == chr) {
                    count++;
                }
            }
            return count;
        }
        public static class Point {
            double x;
            double y;
            Point(double x, double y) {
                this.x = x;
                this.y = y;
            }
        }
        public static class Line {
            Point pt0;
            Point pt1;
            Line(Point pt0, Point pt1) {
                this.pt0 = pt0;
                this.pt1 = pt1;
            }
            public double len() {
                return Math.sqrt(Math.pow((this.pt1.x - this.pt0.x), 2) + Math.pow((this.pt1.y - this.pt0.y), 2));
            }
            public Point midPnt() {
                return new Point(
                    (this.pt0.x + this.pt1.x) / 2, (this.pt0.y + this.pt1.y) / 2
                );
            }
    
        }
    }
    */
    public static void main(String[] args) throws IOException {
        try (FileOutputStream output = new FileOutputStream("temp.txt")) {
            for (int i = 0; i <= 100; i++) {
                int rando = (int)(Math.random() * 10);
                byte comma = 44;
                output.write(rando);
                output.write(comma);
            }
        }

        try (FileInputStream input = new FileInputStream("temp.txt");) {
            int value;
            while ((value = input.read()) != -1) {
                if (value != 44) {
                    System.out.print(value);
                }
            }
        }
    }
}
