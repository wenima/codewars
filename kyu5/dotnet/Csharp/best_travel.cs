// Solution for https://www.codewars.com/kata/best-travel/train/csharp

using System;
using System.Collections.Generic;
using System.Linq;

public static class IterTools
{
  public static IEnumerable<T[]> Combinations<T>(this IList<T> argList, int argSetSize)
  {
    if (argList == null) throw new ArgumentNullException("argList");
    if (argSetSize <= 0) throw new ArgumentException("argSetSize must be great than 0", "argSetSize");
    return combinationsImpl(argList, 0, argSetSize - 1);
  }

  private static IEnumerable<T[]> combinationsImpl<T>(IList<T> argList, int argStart, int argIteration, List<int> argIndices = null)
  {
    argIndices = argIndices ?? new List<int>();
    for (int i = argStart; i < argList.Count; i++)
    {
      argIndices.Add(i);
      if (argIteration > 0)
      {
        foreach (var array in combinationsImpl(argList, i + 1, argIteration - 1, argIndices))
        {
          yield return array;
        }
      }
      else
      {
        var array = new T[argIndices.Count];
        for (int j = 0; j < argIndices.Count; j++)
        {
          array[j] = argList[argIndices[j]];
        }
        yield return array;
      }
      argIndices.RemoveAt(argIndices.Count - 1);
      }
    }
}

public static class SumOfK
{
    public static int? chooseBestSum(int t, int k, List<int> ls) {
        int best = 0;
        var combinations = IterTools.Combinations(ls, k);
        foreach (var c in combinations)
        {
          best = (c.Sum() > best && c.Sum() <= t) ? c.Sum() : best;
        }
        if (best > 0)
        {
          return best;
        }
        else
        {
        return null;
        }
    }
}

// Combinations using LINQ
using System.Collections.Generic;
using System.Linq;

public static class SumOfK
{
  public static int? chooseBestSum(int t, int k, List<int> ls) =>
    ls.Combinations(k)
      .Select(c => (int?) c.Sum())
      .Where(sum => sum <= t)
      .DefaultIfEmpty()
      .Max();

  // Inspired by http://stackoverflow.com/questions/127704/algorithm-to-return-all-combinations-of-k-elements-from-n
  public static IEnumerable<IEnumerable<int>> Combinations(this IEnumerable<int> ls, int k) =>
    k == 0 ? new[] { new int[0] } :
      ls.SelectMany((e, i) =>
        ls.Skip(i + 1)
          .Combinations(k - 1)
          .Select(c => (new[] {e}).Concat(c)));
}

//Shortest solution
using System;
using System.Collections.Generic;
using System.Linq;

public static class SumOfK
{
  public static int? chooseBestSum(int t, int k, List<int> ls)
  {
    var _ls = ls.Where(x => x <= t);
    return _ls.Count() == 0 ? null : _ls.Select((x, i) => x + (k > 1 ? chooseBestSum(t-x, k-1, _ls.Skip(i+1).ToList()) : 0)).Max();
  }
}
