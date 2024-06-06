import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for(int i=1; i<=(2*n-1) ; i++){
            int num = i>n ? 2*n-i : i;
            for(int j=1; j<= n-num; j++){
                System.out.print(" ");
            }
            for(int k=1; k<=num; k++){
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}