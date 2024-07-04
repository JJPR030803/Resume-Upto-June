import java.util.Scanner;

public class switch2 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Ingresa tu calificacion:");
        String grado = in.nextLine().toUpperCase();

        switch(grado){
            case "A+","A"->{
                System.out.println("Distinction");
                System.out.println("Bien Hecho");
            }
        }
    }
}
