public class Program_04 {

    static int Fibonacci(int n)
    {
        if(n<2)
        {
            return n;
        }
        return Fibonacci(n-2)+Fibonacci(n-1);
    }

    public static void main(String[] args) {
        int result;
        result=Fibonacci(6);
        System.out.println("Fibonacci : "+result);
    }
}
