using System;
using System.Collections.Generic;
using System.Text;

namespace PokerRankingsSolution
{

    class Constants
    {
        private readonly Dictionary<string, Tuple<string, int>> ranks = new Dictionary<string, Tuple<string, int>>()
        {
            { "A", new Tuple<string, int>("Ace", 14) },
            { "K", new Tuple<string, int>("King", 13) },
            { "Q", new Tuple<string, int>("Queen", 12) },
            { "J", new Tuple<string, int>("Jack", 11) },
            { "T", new Tuple<string, int>("Ten", 10) },
            { "9", new Tuple<string, int>("Nine", 9) },
            { "8", new Tuple<string, int>("Eight", 8) },
            { "7", new Tuple<string, int>("Seven", 7) },
            { "6", new Tuple<string, int>("Six", 6) },
            { "5", new Tuple<string, int>("Five", 5) },
            { "4", new Tuple<string, int>("Four", 4) },
            { "3", new Tuple<string, int>("Three", 3) },
            { "2", new Tuple<string, int>("Two", 2) },
        };
    }
    class PokerHand
    {
        public string hand { get; set; }
        private TupleList<string, int> HighCards { get; set; }
        public string[] vals { get; set; }

        public PokerHand(string hand)
        {
            hand = hand.Trim();
            HighCards = new TupleList<string, int>();
        }

    }
}
