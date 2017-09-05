using System;
using System.Collections.Generic;
using System.Text;

namespace PokerRankingsSolution
{
    public static class Helper
    {
        public static IEnumerable<KeyValuePair<int, T>> Enumerate<T>(this IEnumerable<T> collection, int startIndex=0)
        {
            foreach (var item in collection) { yield return new KeyValuePair<int, T>(startIndex++, item); }
        }
    }

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
        private TupleList<string, int> hand { get; } = new TupleList<string, int>();
        private List<char> vals { get; } = new List<char>();
        private static List<char> suits {get; } = new List<char>();
        private Dictionary<char, int> val_cnt { get; }
        private int handvalue { get; }
        private List<char> twoPair { get; }
        private bool isFlush { get; } = (suits.Distinct().Count() == 1);
        private bool isStraight { get; }
        

        public string CompareWith(PokerHand hand)
        {
            if (this.handvalue > hand.handvalue) { return "Win"; }
            else if (this.handvalue < hand.handvalue) { return "Loss"; }
            else
            {
                foreach (var idx_card in Helper.Enumerate(this.hand))
                {
                    int idx = idx_card.Key;
                    if (idx_card.Value.Item2 > hand.hand[idx].Item2) { return "Win "; }
                    else if (idx_card.Value.Item2 < hand.hand[idx].Item2) { return "Loss"; }
                 }
                 return "Tie";
            }
        }

        public PokerHand(string hand)
        {
            hand = hand.Trim();
            this.handvalue = 0;
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
                    this.suits.Add(card);
                }
            }
            // initializing isFlush property
            this.isFlush = (this.suits.Distinct().Count() == 1) ? true : false;
            // initializing isStraight property; default value is true
            this.hand.Sort((x, y) => y.Item2.CompareTo(x.Item2));
            int prev_card = this.hand[0].Item2 + 1;
                foreach (Tuple<string, int>card in this.hand)
                {
                    if (prev_card - 1 != card.Item2)
                    {
                        this.isStraight =  false;
                    }
                    prev_card = card.Item2;
                }
            // count how often a card appears to get all pairs, sets and quads
            var groups = vals.GroupBy(c => c )
                            .Select(c => new { Vals = c.Key, Count = c.Count() });
            val_cnt = groups.ToDictionary( g => g.Vals, g => g.Count);
            // checking if hand contains 2pair
            this.twoPair = new List<char>();
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
            // setting final handvalue
            if (this.handvalue != 3) 
            {
                if (this.isStraight)
                {
                    this.handvalue = (this.isFlush) ? 9 : 5;
                }
                if (this.handvalue == 0 && this.isFlush)
                {
                    this.handvalue = 6;
                }
                foreach (KeyValuePair<char, int>card in ordered_val_cnt)
                {
                    switch(card.Value)
                    {
                        case 4:
                            this.handvalue = 8;
                            break;
                        case 3:
                            this.handvalue = 4;
                            break;
                        case 2:
                            if (this.handvalue == 4)
                            {
                                this.handvalue = 7;
                            }
                            this.handvalue = 1;
                            break;
                        default:
                            break;
                    }   
                }
            }

        }
    }
}
