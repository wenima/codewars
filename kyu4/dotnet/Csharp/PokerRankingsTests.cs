using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using NUnit.Framework;

namespace PokerRankingsSolution
{
    [TestFixture]
    public class KataTests
    {
        [Test]
        public void TestHandIsAStraight()
        {
            var HeroesHand = new PokerHand("2H 3H 4H 5H 6S");
            Assert.That(delegate { HeroesHand.IsStraight(); }, Is.EqualTo(true));
        }

        [Test]
        public void TestHandIsAFlush()
        {
            var HeroesHand = new PokerHand("AS 3S 4S 8S 2S");
            Assert.That(delegate { HeroesHand.IsFlush(); }, Is.EqualTo(true));
        }

        [Test]
        public void TestHandHasCorrectHighCard()
        {
            var HeroesHand = new PokerHand("8H 9H QS JS KH");
            HeroesHand.setHighCards();
            Assert.That(delegate { HeroesHand.HighCards.pop()[0]; }, Is.EqualTo("K"));
            Assert.That(delegate { HeroesHand.HighCards.pop()[0]; }, Is.EqualTo("Q"));
        }

        [Test]
        public void TestCompareHeroToVillain()
        {
            var HeoresHand = new PokerHand("2H 3H 4H 5H 6H");
            var VillainsHand = new PokerHand("KS AS TS QS JS");

        }
    }
}
