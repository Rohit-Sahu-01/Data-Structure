
public class Program_02 {
    static int exponential(int x,int p)
    {
      if (p<1) return 1;
      return x * exponential(x, p-1);
    }

    public static void main(String[] args) {
        int result=exponential(2, 1);
        System.out.println("Exponential : "+result);
    }
}
