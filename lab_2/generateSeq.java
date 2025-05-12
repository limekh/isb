import java.security.SecureRandom;

public class Main {
    public static void main(String[] args) {
        String binarySequence = generate128BitBinaryString();
        System.out.println(binarySequence);
    }
    public static String generate128BitBinaryString() {
        SecureRandom random = new SecureRandom();
        StringBuilder sb = new StringBuilder(128);

        for (int i = 0; i < 128; i++) {
            sb.append(random.nextBoolean() ? '1' : '0');
        }

        return sb.toString();
    }
}