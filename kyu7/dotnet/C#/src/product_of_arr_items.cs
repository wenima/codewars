// Solution for kata https://www.codewars.com/kata/product-of-array-items/

public static int Product(int[] values)
    {
      return values.Aggregate((a, b) => a * b);
    }
