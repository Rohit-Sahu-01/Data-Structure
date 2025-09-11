public class Program_03 {

   
    static int Factorial(int n)
    {
        if(n<=1)
        {
            return 1; 
        }
        return Factorial(n-1) * n ;
    }

    public static void main(String[] args) {
        int result;
        result=Factorial(5);
        System.out.println("Factorial : "+result);

    }
}
