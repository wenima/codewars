// Solution for kata https://www.codewars.com/kata/climbers-rankings/
// Comment: the return type for this kata is set to be a dict when it should really be
// an array as order is not guaranteed for a dict, OrderedDictionary in C# only sorts by value
// which isn't what is required here.

using System;
using System.Collections.Generic;
using System.Linq;

namespace ClimbersRanking
{
    public static class RankCalculator
    {
        public static Dictionary<string, int> GetRankings(Dictionary<string, IEnumerable<int>> pointsByClimber)
        {
          var d = new Dictionary<string, int>();
          foreach (KeyValuePair<string, IEnumerable<int>> entry in pointsByClimber)
          {
            List<int> all_points = new List<int>();
            all_points = entry.Value.ToList();
            all_points.Sort((a, b) => -1 * a.CompareTo(b));
            int points = 0;
            int end = all_points.Count() >= 6 ? 6 : all_points.Count();
            for (int idx = 0; idx < end; idx++)
            {
              points += all_points[idx];
            }
            d.Add(entry.Key, points);
          }
          var out_list = d.ToList();
          out_list.Sort((x, y) => y.Value.CompareTo(x.Value));
          d = out_list.ToDictionary(pair => pair.Key, pair => pair.Value);
          return d;
        }
    }
}

// more concise way:
public static class RankCalculator
    {
        public static Dictionary<string, int> GetRankings(Dictionary<string, IEnumerable<int>> pointsByClimber)
        {
          return pointsByClimber
                .ToDictionary(x => x.Key, x => x.Value.OrderByDescending(y => y).Take(6).Sum())
                .OrderByDescending(x => x.Value)
                .ToDictionary(x => x.Key, x => x.Value);
        }
    }
