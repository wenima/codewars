// Solution for kata https://www.codewars.com/kata/sort-an-array-by-value-and-index/

using System;
using System.Collections.Generic;
using System.Linq;

public class Kata
{
  public static int[] SortByValueAndIndex(int[] array)
  {
    array.ToList().ForEach(Console.WriteLine);
    var tuple_lst = new List<Tuple<string, int, int>>();
    foreach (int n in array)
    {
      string t_name = n.ToString();
      var tuple = new Tuple<string, int, int>(t_name, n, (Array.IndexOf(array, n) + 1) * n);
      tuple_lst.Add(tuple);
    }
    tuple_lst.Sort((x, y) => x.Item3 - y.Item3);
    var ret_lst = new List<int>();

    foreach (var n in tuple_lst)
    {
      ret_lst.Add(n.Item2);
    }
    return ret_lst.ToArray();
  }
}
