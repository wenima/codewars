using System;
using System.Collections.Generic;
using System.Text;

namespace PokerRankingsSolution
{

    class Constants
    {
        private readonly Dictionary<string, Tuple<string, int>> Ranks = new Dictionary<string, Tuple<string, int>>()
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
        private readonly Dictionary<string, Tuple<string, int>> Suits = new Dictionary<string, Tuple<string, int>>()
        {
            { "S": ('Spades', 1) },
            { "H": ('Hearts', 1) },
            { "D": ('Diamonds', 1) },
            { "C": ('Clubs') }
        };
        private readonly Dictionary<string, int> MadeHands = new Dictionary<string, int>()
        {
            { "Straight Flush", 9 },
            { "4 of a Kind", 8 },
            { "Full House", 7 },
            { "Flush", 6 },
            { "Straight", 5 },
            { "Set", 4 },
            { "Two Pair", 3 },
            { "One Pair", 1 },
            { "High Car", 0 }
        };
    }
    class PokerHand
    {
        public TupleList<string, int> hand { get; set; }
        public TupleList<string, int> HighCards { get; set; }
        public string[] vals { get; set; }
        public string[] suits {get; set; }
        public Dictionary<string, int> val_cnt { get; set; }
        public List<int> twopair { get; set; }
        public int handvalue { get; set; }

        public PokerHand(string hand)
        {
            hand = hand.Trim();
            this.HighCards = new TupleList<string, int>();
            foreach (var card in hand)
            {
                if (Ranks.ContainsKey(card))
                    {
                        this.vals.Add(card);
                        this.hand.Add(card, Ranks[card][1])
                    }
            }
            foreach (var card in Hand)
            {
                if (Suits.ContainsKey(card))
                {
                    this.suits.Add(Suits[card])
                }
            }
            this.hand.Sort((x, y) => y.Item1.CompareTo(x.Item1));
            foreach (card in vals)
            {
                var groups = vals.GroupBy(c => c )
                                        .Select(c => new { Vals = c.Key, Count = c.Count() });
            }
            val_cnt = groups.ToDictionary( g => g.Vals, g => g.Count);
            handvalue = 0;
        }

    }
}
