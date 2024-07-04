import java.util.Scanner;

public class ifstatement {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("\nIngresa tu edad:");
        int edad = in.nextInt();

        if (edad < 0 || edad > 100){
            System.out.println("Edad invalilda");
        }
        else if(edad<18){
            System.out.println("Eres menor de edad");
        }else if(edad<21){
            System.out.println("Necesitas consentimiento de tus padres");
        }else{
            System.out.println("Felicidades, puedes inscribirte al evento.");
        }
    }
}
