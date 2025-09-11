class Program_01
{

    static int Sum(int n)
    {
        if(n<=0) return 0;
        return Sum(n-1)+n;
    }

    public static void main(String[] args) {
        int r=Sum(20);
        System.out.println("Sum : "+r);

    }
}