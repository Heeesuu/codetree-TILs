import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        if(n>2){
            for(int i=1; i<=n; i++){
                System.out.print("* ");
            }
            System.out.println();
            for(int j=1; j<=n-2; j++){
                for(int k=1; k<=j; k++){
                    System.out.print("* ");
                }
                for(int m=(n-j-1); m>=1; m--){
                    System.out.print("  ");
                }
                System.out.println("*");
            }

            for(int i=1; i<=n; i++){
                System.out.print("* ");
            }
        }else{
            for(int i=1; i<=n; i++){
                for(int j=1; j<=n; j++){
                    System.out.print("* ");
                }
                System.out.println();    
            }
        }
    }
}