using System;
using System.Collections.Generic;
using System.Text;

namespace PokerRankingsSolution
{

    class Constants
    {
        public static readonly Dictionary<char, Tuple<string, int>> Ranks = new Dictionary<char, Tuple<string, int>>()
        {
            { 'A', new Tuple<string, int>("Ace", 14) },
            { 'K', new Tuple<string, int>("King", 13) },
            { 'Q', new Tuple<string, int>("Queen", 12) },
            { 'J', new Tuple<string, int>("Jack", 11) },
            { 'T', new Tuple<string, int>("Ten", 10) },
            { '9', new Tuple<string, int>("Nine", 9) },
            { '8', new Tuple<string, int>("Eight", 8) },
            { '7', new Tuple<string, int>("Seven", 7) },
            { '6', new Tuple<string, int>("Six", 6) },
            { '5', new Tuple<string, int>("Five", 5) },
            { '4', new Tuple<string, int>("Four", 4) },
            { '3', new Tuple<string, int>("Three", 3) },
            { '2', new Tuple<string, int>("Two", 2) },
        };
        public static readonly Dictionary<char, Tuple<string, int>> Suits = new Dictionary<char, Tuple<string, int>>()
        {
            { 'S', new Tuple<string, int>("Spades", 1) },
            { 'H', new Tuple<string, int>("Hearts", 1) },
            { 'D', new Tuple<string, int>("Diamonds", 1) },
            { 'C', new Tuple<string, int>("Clubs", 1) }
        };
        public static readonly Dictionary<string, int> MadeHands = new Dictionary<string, int>()
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
        public TupleList<string, int> hand { get; set; } = new TupleList<string, int>();
        public TupleList<string, int> HighCards { get; set; }
        public List<char> vals { get; set; } = new List<char>();
        public List<char> suits {get; set; } = new List<char>();
        public Dictionary<char, int> val_cnt { get; set; }
        rivate List<char> twoPair { get; }
        public int handvalue { get; set; }
        public bool isFlush 
        {
            get 
            {
                if (suits.Distinct().Count() == 1) 
                {
                    return true;
                }
                return false;
            }
        }
        public bool isStraight
        {
            get
            {   
                int prev_card = this.hand[0].Item2 + 1;
                foreach (var card in this.hand)
                {
                    if ((prev_card -= 1) != card.Item2)
                    {
                        return false;
                    }
                    prev_card = card.Item2;
                }
                return true;
            }
        }


        public PokerHand(string hand)
        {
            hand = hand.Trim();
            this.HighCards = new TupleList<string, int>();
            foreach (var card in hand)
            {
                if (Constants.Ranks.ContainsKey(card))
                    {
                        this.vals.Add(card);
                        this.hand.Add(card.ToString(), Constants.Ranks[card].Item2);
                    }
            }
            foreach (var card in hand)
            {
                if (Constants.Suits.ContainsKey(card))
                {
                    suits.Add(card);
                }
            }
            this.hand.Sort((x, y) => y.Item1.CompareTo(x.Item1));
            var groups = vals.GroupBy(c => c )
                            .Select(c => new { Vals = c.Key, Count = c.Count() });
            val_cnt = groups.ToDictionary( g => g.Vals, g => g.Count);
            handvalue = 0;
            his.twoPair = new List<char>();
            var ordered_val_cnt = val_cnt.OrderBy(x => x.Value);
            foreach (KeyValuePair<char, int>card in ordered_val_cnt)
            {
                if (card.Value == 2) 
                {
                    if (this.twoPair.Count  == 1)
                    {
                        this.twoPair.Add(card.Key);
                        this.handvalue += 3;
                        break;
                    }
                    this.twoPair.Add(card.Key);
                }
            }
        }
    }
}
