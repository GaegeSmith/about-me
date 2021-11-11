import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.util.Scanner;

public class BufferWriter {
    
    // global variables
    private static final String DATA_FILE = "mymedia.txt";
    private static Scanner in;
    private static BufferedWriter out;
    
    // writeString
    public static void writeString(String s) {
        // check to see if out is assigned
        if (out == null) {
            try {
                out = new BufferedWriter(new FileWriter(DATA_FILE));
            } catch (Exception e) {
                System.err.println("Cannot open file for output!");
                e.printStackTrace();
            }
        }

        try {
            out.write(s);
            out.newLine();
        } catch (Exception e) {
            System.err.println("Cannot write file!");
            e.printStackTrace();
        }
    }
    
    // saveAndClose
    public static void saveAndClose() {
        // closes after the Scanner is done reading flie
        if (in != null) {
            try {
                in.close();
                in = null;
            } catch (Exception e) {
                System.err.println("Cannot close input file!");
                e.printStackTrace();
            }
        }

        // closes after the BufferedWriter is done writing to the file
        if (out != null) {
            try {
                out.close();
                out = null;
            } catch (Exception e) {
                System.err.println("Cannot close output file!");
                e.printStackTrace();
            }
        }
    }
    
    // readString
    public static String readString() {
        String urMom = null;
        if (in == null) {
            try {
                in = new Scanner(new File(DATA_FILE));
            } catch (Exception e) {
                System.err.println("Cannot open file for input!");
                e.printStackTrace();
            }
        }

        try {
            // check if in hasNext line
            if (in.hasNext()) {
                String s = in.nextLine();
                return s; // grabing everything
            }
        } catch (Exception e) {
            System.err.println("I cannot read!");
            e.printStackTrace();
        }

        return urMom;
    }
}
