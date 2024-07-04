import java.util.Scanner;

public class switchst {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Ingresa tu calificacion:");
        String grado = in.nextLine().toUpperCase();

        switch (grado) {
            case "A+":
            case "A":
            System.out.println("Muy bien Felicidades!");
                break;
            case "B":
            System.out.println("Obtuviste un B");
            break;
            case "C":
            System.out.println("Obtuviste un C");
            break;
            default:
            System.out.println("Reprobaste:(");
                break;
        }
    }
}
