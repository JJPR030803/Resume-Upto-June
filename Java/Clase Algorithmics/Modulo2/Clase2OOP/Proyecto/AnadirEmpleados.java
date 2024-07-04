package Modulo2.Clase2OOP.Proyecto;


public class AnadirEmpleados {
    static Staff empleado1 = new Staff("Juan", 8);
    public static void main(String[] args) {
        Staff empleado2 = new Staff("Pedrito", 10);
        empleado1.setHorasTrabajadas(9);
        double paga = empleado1.calcularPago();
        double paga2 = empleado2.calcularPago();
        System.out.println(paga);
        System.out.println(paga2);
    }
}
