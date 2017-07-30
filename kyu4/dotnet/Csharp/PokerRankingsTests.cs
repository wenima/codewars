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
            var heros_hand = new PokerHand<string> { "2H 3H 4H 5H 6S" };
            Assert.That(delegate { PokerHand.IsStraight(); }, Is.EqualTo(true));
        }
    }
}
