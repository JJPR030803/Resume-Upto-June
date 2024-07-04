package Modulo2.Clase2OOP;

public class constructores {
    private String name;
    private final int hourlyRate = 30;
    private int horasTrabajadas;
    public constructores(String nombre){
        name = nombre;
    }
    public constructores(String primerNombre,String segundoNombre){
        name = primerNombre+""+segundoNombre;
    }
    public static void main(String[] args) {
    }
    public void printMessage(){
        System.out.println("Calculando pago...");
    }
    public int calcularPago(){
        printMessage();
        int pagoStaff;
        pagoStaff = horasTrabajadas*hourlyRate;
        if(horasTrabajadas>0){
            return pagoStaff;
        }else{
            return -1;
        }
    }
    public int calcularPago(int bonus,int allowance){
        printMessage();
        if (horasTrabajadas>0) {
            return horasTrabajadas*hourlyRate+bonus+allowance;
        }else{
            return 0;
        }
    }
    public void setHorasTrabajadas(int horas){
        if (horas>0) {
            horasTrabajadas = horas;
        }else{
            System.out.println("Error: Horas Trabajadas no pueden ser menores a 0.");
            System.out.println("Horas Trabajadas no sera actualizado");
        }
    }
    public int getHorasTrabajadas(){
        return horasTrabajadas;
    }
}
