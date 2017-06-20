// Solution for kata https://www.codewars.com/kata/sum-of-all-the-multiples-of-3-or-5/

{
  public static class Program
  {
    public static int findSum(int n)
    {
      int sum = 0;
      for (int counter = 0; counter <= n; counter++)
      {
        sum = ((counter % 3 == 0) || (counter % 5 == 0)) ? sum += counter : sum;
      }
      return sum;
    }
  }
}
