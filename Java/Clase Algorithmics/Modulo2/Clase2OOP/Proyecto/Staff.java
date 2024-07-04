package Modulo2.Clase2OOP.Proyecto;

public class Staff {
    private String nombreEmpleado;
    private final int pagoHora = 30;
    private int horasTrabajadas;

    public Staff(String nombre,int Horas){
        nombreEmpleado = nombre;
        horasTrabajadas = Horas;
    }

    public void setHorasTrabajadas(int horasTrabajadas) {
        try {
            if (horasTrabajadas>0) {
                this.horasTrabajadas = horasTrabajadas;
            }else{
                System.out.println("No puede ser un valor menor a 0");
            }
        } catch (Exception e) {
            // TODO: handle exception
        }
        
        
    }
    public void setNombreEmpleado(String nombreEmpleado) {
        this.nombreEmpleado = nombreEmpleado;
    }
    public int getHorasTrabajadas() {
        return horasTrabajadas;
    }
    public String getNombreEmpleado() {
        return nombreEmpleado;
    }
    public int getPagoHora() {
        return pagoHora;
    }
    public double calcularPago(){
       return this.horasTrabajadas * this.pagoHora;
    }
}
