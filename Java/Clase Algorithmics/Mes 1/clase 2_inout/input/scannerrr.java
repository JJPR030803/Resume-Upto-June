import java.util.Scanner;

public class scannerrr {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Ingresa un numero:");
        int myInt = input.nextInt();
        System.out.printf("Numero entero: %d. \n", myInt);

        double myDouble = myDouble = input.nextDouble();
        System.out.printf("Ingresaste: %.2f.\n",myDouble);


        input.nextLine();
        System.out.println("Ingresa un texto:");
        String myString = input.nextLine();
        System.out.printf("Has ingresado: \"%s\"", myString);
    }
}
