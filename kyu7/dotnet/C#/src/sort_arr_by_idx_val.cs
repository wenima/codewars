// Solution for kata https://www.codewars.com/kata/sort-an-array-by-value-and-index/

using System;
using System.Collections.Generic;
using System.Linq;

public class Kata
{
  public static int[] SortByValueAndIndex(int[] array)
  {
    arr.ToList().ForEach(Console.WriteLine);
    int i = 1;
    var tuple_lst = new List<Tuple<string, int, int>>();
    foreach (int n in array)
    {
      string t_name = n.ToString();
      var tuple = new Tuple<string, int, int>(t_name, n, i * n);
      tuple_lst.Add(tuple);
      i++;
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

// highest voted
  public static int[] SortByValueAndIndex(int[] array)
  {
    int i = 1;
    return array.OrderBy(n => n * i++).ToArray();
  }

// using a for loop and index

  public static int[] SortByValueAndIndex(int[] array)
  {
    int[] keys = new int[array.Length];
    for (int i = 0; i < array.Length; i++) keys[i] = array[i] * (i + 1);
    Array.Sort(keys, array);
    return array;
  }

// using tuples and Linq

  public static int[] SortByValueAndIndex(int[] array)
  {
      var tuples = array.Select((t, i) => new Tuple<int, int>(t, (i + 1) * t)).ToList();
        return tuples.OrderBy(x => x.Item2).ToList().Select(x => x.Item1).ToArray();
  }
