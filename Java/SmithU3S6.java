import java.util.Scanner;
import java.lang.Math;

public class SmithU3S6 {
    public class Useful {
        public static void main(String[] args) {
            System.out.println("Useful");
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


    public static void main(String[] args){
        // int[] nums = {1, 2, 3, 2, 1, 6, 3, 4, 5, 2, 3, 6, 8, 9, 9, 0};
        // evenOddChecker(nums);
        int[] lst0 = {1, 5, 16, 61, 111};
        int[] lst1 = {2, 4, 5, 6};
        int[] lst01 = merge(lst0, lst1);
        // for (int i : lst01) {
        //     System.out.println("" + i);
        // }
        int[] notSorted = {10, 1, 5, 16, 61, 9, 11, 1};
        int[] sorted = {21, 11, 9, 7, 5, 4, 4, 3, 1, 1};
        System.out.println(isSorted(notSorted));
        System.out.println(isSorted(sorted));

        // work in progress
        // bean();
    }

    public static void evenOddChecker(int[] listy) {
        int even = 0;
        int odd = 0;
        for (int i = 0; i < listy.length; i++) {
            if (listy[i] != 0) {
                if (listy[i] % 2 == 0) {
                    even++;
                } else {
                    odd++;
                }
            }
        }
        System.out.printf("The number of odd numbers: %d\n", odd);
        System.out.printf("The number of even numbers: %d\n", even);
    }
    
    // swap values at ind1 and ind2
    public static int[] swap(int[] listy, int ind1, int ind2) {
        int[] result = listy;
        int tmp = listy[ind1];
        result[ind1] = listy[ind2];
        result[ind2] = tmp;
        return result;
    }
    
    public static int[] merge(int[] list1, int[] list2) {
        int[] result = new int[list1.length + list2.length];
        int prevInd = 0;
        boolean swapped = true;
        boolean allowToggle = true;

        // combines the lists
        for (int i = 0; i < result.length; i++) {
            if (i >= list1.length) {
                result[i] = list2[(i - list1.length)];
            } else {
                result[i] = list1[i];
            }
        }

        // loops until no swaps happen, aka the list is sorted
        while (swapped) {
            prevInd = 0;
            // loop through list
            for (int i = 0; i < result.length; i++) {
                // if the current number is less than previous number, swap them and lock the swapped to true
                if (result[i] < result[prevInd]) {
                    result = swap(result, i, prevInd);
                    swapped = true;
                    allowToggle = false;
                } else if (allowToggle) {
                    swapped = false;
                }

                prevInd = i;
            }
            // unlock swapped value
            allowToggle = true;
            
        }

        return result;
    }

    public static boolean isSorted(int[] lst) {
        int prevInd = 0;
        for (int i = 0; i < lst.length; i++) {
            if (lst[i] > lst[prevInd]) {
                return false;
            }

            prevInd = i;
        }
        return true;
        
    }
    // work in progress
    // public static void bean() {
    //     Scanner ui = Useful.newScanner();
    //     System.out.print("")
    //     int ballCnt = ui.nextInt();
    //     int lvlCnt = ui.nextInt();
    //     Ball[] balls = new Ball[ballCnt];
    //     for (int i = 0; i < balls.length; i++) {
    //         balls[i] = new Ball(lvlCnt);
    //     }
        


    // }

}