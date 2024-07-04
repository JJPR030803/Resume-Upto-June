import java.util.Arrays;

public class array_meth {
    public static void main(String[] args) {
        int[] arr1 = {0,2,4,6,8,10};
        int[] arr2 = {0,2,4,6,8,10};
        int[] arr3 = {10,8,6,4,2,0};

        boolean result1 = Arrays.equals(arr1, arr2);
        boolean result2 = Arrays.equals(arr1, arr2);

        int[] source = {12,1,5,-2,16,14,18};

        int[] nuevo = Arrays.copyOfRange(source, 3, 7);

        int[] numeros = {1,2,3,4,5};
        int[] numeros2 = {12,1,512,4,16,-1};
        Arrays.sort(numeros2);


        int[] lista1 = {21,23,34,45,56,78,99};
        int longitud = lista1.length;
        int indiceEncontrado = Arrays.binarySearch(lista1, 78);


        System.out.println(Arrays.toString(numeros2));
        System.out.println(result1+"\n"+result2);
        System.out.println(indiceEncontrado);
    }
    
}
