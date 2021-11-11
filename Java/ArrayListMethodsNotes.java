import java.util.ArrayList;
import java.util.Scanner;


public class ArrayListMethodsNotes {
    public class Useful {
        public static void main(String[] args) {
            System.out.println("\n\tNobody:\n\tJava:");
            int bigest = 2147483647;
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

    public static void main(String[] args) {
        ArrayList<Integer> arrList = new ArrayList<Integer>();
        int[] arr = {1, 2, 0, 3, 2, 4, 2, 1, 0, 1, 3, 2};

        System.out.println(System.currentTimeMillis());
        System.out.println(mode(createArrayList(arr)));
        System.out.println(System.currentTimeMillis());
    }

    public static ArrayList<Integer> createArrayList(int[] input) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        for (int i = 0; i < input.length; i++) {
            result.add(input[i]);
        }
        return result;
    }

    public static int minIntAL(ArrayList<Integer> temp) {
        int min = 0;
        for (int i = 0; i < temp.size(); i++) {
            if (i == 0) {
                min = temp.get(i);
            } else if (temp.get(i) < min) {
                min = temp.get(i);
            }
        }
        return min;
    }

    public static int maxIntAL(ArrayList<Integer> temp) {
        int max = 0;
        for (int i = 0; i < temp.size(); i++) {
            if (i == 0) {
                max = temp.get(i);
            } else if (temp.get(i) > max) {
                max = temp.get(i);
            }
        }
        return max;
    }

    public static int aveIntAL(ArrayList<Integer> temp) {
        int ave = 0;
        for (int i = 0; i < temp.size(); i++) {
            ave += temp.get(i);
        }
        return ave / temp.size();
    }

    // Determine the frequency of a certain property; return -1 if no exist
    public static int count(ArrayList<Integer> temp, int valueToCheck) {
        int count = 0;
        // for each
        for (int i: temp) {
            if (i == valueToCheck) {
                count++;
            }
        }

        if (count != 0) {
            return count;
        }
        return -1;
    }

    public static ArrayList<Integer> rmDupe(ArrayList<Integer> temp) {
        ArrayList<Integer> out = new ArrayList<Integer>();
        for (int i : temp) {
            if (!out.contains(i)) {
                out.add(i);
            }
        }
        return out;
    }

    public static int mode(ArrayList<Integer> temp) {
        ArrayList<Integer> vals = rmDupe(temp);
        ArrayList<Integer> count = new ArrayList<Integer>();
        int mode = 0;
        for (int i = 0; i < vals.size(); i++) {
            count.add(
                count(temp, vals.get(i))
            );
            if (i == 0) {
                mode = vals.get(i);
            } else if (count.get(vals.indexOf(mode)) < maxIntAL(count)) {
                mode = vals.get(
                    count.indexOf(
                        maxIntAL(count)
                    )
                );
            }
        }

        return mode;
    }

}
