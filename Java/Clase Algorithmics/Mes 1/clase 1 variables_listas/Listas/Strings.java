

public class Strings {

    public static void main(String[] args) {
        String mensaje = "Hola Mundo";
        String hola = "Hola";
        String mundo = "Mundo";
        String HolaMundo = hola+mundo;



        int longitud = "Hola Mundo".length();
        String mayuscula = "Hola Mundo".toUpperCase();
        String subString = "Hola Mundo".substring(5);
        char myChar ="Hola Mundo".charAt(longitud-1);
        boolean esJaime = "Hola soy Jaime".equals("Jaime");
        String nombres = "Pedrito,Juan,Anakin,Maria";
        String[] separaString = nombres.split(",");


        System.out.println(longitud);
        System.out.println(mayuscula);
        System.out.println(subString);
        System.out.println(esJaime);

    }
    
}
