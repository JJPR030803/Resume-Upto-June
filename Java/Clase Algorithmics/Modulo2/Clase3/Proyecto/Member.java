package Modulo2.Clase3.Proyecto;
import java.util.Scanner;
public class Member {
    public String bienvenido = "Bienvenido al ABC fitness";
    protected double anualidad;
    private String nombre;
    private int miembroID;
    private int miembroDesde;
    private int descuento;

    public Member(){
        System.out.println();
    }

    public Member(String pName,int pMemberID,int pMiembroDesde){
        nombre = pName;
        miembroID = pMemberID;
        miembroDesde = pMiembroDesde;
    }

    public double getDescuento(){
        return descuento;
    }
    public void setDescuento(){
        Scanner in = new Scanner(System.in);
        String contrasena;
        System.out.println("Ingrese la contraseña:");
        contrasena = in.nextLine();
        if (!contrasena.equals("abcd")) {
            System.out.println("Contraseña Invalida");
        }
    }
}
