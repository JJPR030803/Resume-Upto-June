

public class branchStatements {
    public static void main(String[] args) {
        int counter = 8;
        for(int i =0;i<counter;i++){
            System.out.println(counter);
            if(counter == 2){
                System.out.println("El numero es 2");
            }else if(counter == 7){
                break;
            }
        }
    }
}
