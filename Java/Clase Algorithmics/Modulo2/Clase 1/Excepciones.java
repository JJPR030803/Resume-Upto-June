import java.util.Scanner;

public class Excepciones {
    public static void main(String[] args) {
        int num,deno;
        Scanner input = new Scanner(System.in);

        try {
            System.out.println("Ingrese el numerador:");
            num = input.nextInt();
            System.out.println("Ahora ingrese el denominador:");
            deno = input.nextInt();
            System.out.printf("El resultado es %d",num/deno);
        } catch (Exception e) {
            System.out.println(e.getMessage()+"Error de no se");
        }
        finally{
            System.out.println("---Fin de manejo de excepciones---");
        }

    }
}
