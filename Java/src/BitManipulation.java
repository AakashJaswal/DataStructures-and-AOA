import java.io.*;

public class BitManipulation {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int i = Integer.parseInt(br.readLine());
        String res = (i & 1) == 0 ? "True":"False";
        System.out.println("Is Even = " + res);
    }
}
