# Generate cubes number pattern from 1 to 10
# 1 8 27 64 ...
import java.util.Scanner;
public class Exercise13 {

   public static void main(String[] args)

{
    int i,n;

    System.out.print("10 : ");
    Scanner in = new Scanner(System.in);
		    n = in.nextInt();

     for(i=1;i<=n;i++)
     {
     System.out.println("Number is : " +i+" and cube of " +i+" is : "+(i*i*i));     
    }
 }
}


