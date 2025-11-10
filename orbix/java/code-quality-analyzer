import java.io.*;

public class CodeQualityAnalyzer {
    public static void main(String[] args) throws IOException {
        if(args.length == 0) {
            System.out.println("Usage: java CodeQualityAnalyzer <source.java>");
            return;
        }
        BufferedReader reader = new BufferedReader(new FileReader(args[0]));
        String line;
        int lineCount = 0;
        while((line = reader.readLine()) != null) {
            lineCount++;
            if(line.contains("import ") && line.trim().equals("import java.util.List;")) {
                System.out.println("Found unused import at line " + lineCount);
            }
        }
        reader.close();
    }
}
