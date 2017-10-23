// Poker Hand Evaluator by Pat Wilson ©2012
hands=["four-of-a-kind", "straight-flush", "straight", "flush", "nothing",
"pair", "two pair", "royal flush", "three-of-a-kind", "full house", "-Invalid-" ];
handRanks = [8,9,5,6,1,2,3,10,4,7,0];
var cardsLookup = {
  2: '2',
  3: '3',
  4: '4',
  5: '5',
  6: '6',
  7: '7',
  8: '8',
  9: '9',
  10: '10',
  11: 'J',
  12: 'Q',
  13: 'K',
  14: 'A'
};

function calcIndex(cs,ss) {
  var v,i,o,s; for (i=-1, v=o=0; i<5; i++, o=Math.pow(2,cs[i]*4)) {v += o*((v/o&15)+1);}
  if ((v%=15)!=5) {return v-1;} else {s = 1<<cs[0]|1<<cs[1]|1<<cs[2]|1<<cs[3]|1<<cs[4];}
  v -= ((s/(s&-s) == 31) || (s == 0x403c) ? 3 : 1);
  return v - (ss[0] == (ss[0]|ss[1]|ss[2]|ss[3]|ss[4])) * ((s == 0x7c00) ? -5 : 1);
}

function getCards(str) {
  var cardStr =  str.replace(/A/g,"14").replace(/K/g,"13").replace(/Q/g,"12")
            .replace(/J/g,"11").replace(/♠|♣|♥|♦/g,",");
  return cardStr.replace(/\s/g, '').slice(0, -1).split(",");
}

function getSuits(str) {
  return str.match(/♠|♣|♥|♦/g);
}

function getCombinations(k,n) {
  var result = [], comb = [];
      function next_comb(comb, k, n ,i) {
          if (comb.length === 0) {for (i = 0; i < k; ++i) {comb[i] = i;} return true;}
          i = k - 1; ++comb[i];
          while ((i > 0) && (comb[i] >= n - k + 1 + i)) { --i; ++comb[i];}
          if (comb[0] > n - k) {return false;} // No more combinations can be generated
          for (i = i + 1; i < k; ++i) {comb[i] = comb[i-1] + 1;}
          return true;
      }
  while (next_comb(comb, k, n)) { result.push(comb.slice());}
  return result;
}

function getPokerScore(cs) {
  var a = cs.slice(), d={}, i;
  for (i=0; i<5; i++) {d[a[i]] = (d[a[i]] >= 1) ? d[a[i]] + 1 : 1;}
  a.sort(function(a,b){return (d[a] < d[b]) ? +1 : (d[a] > d[b]) ? -1 : (b - a);});
  return a[0]<<16|a[1]<<12|a[2]<<8|a[3]<<4|a[4];
}

function rankHand(str) {
  cards = getCards(str);
  suits = getSuits(str);
  var index = 10, winCardIndexes, i ,e, wci;
  for (i=0;i<cards.length;i++) { cards[i]-=0; }
  for (i=0;i<suits.length;i++) { suits[i] = Math.pow(2, (suits[i].charCodeAt(0)%9824)); }
  // console.log('cards: ' + cards);
  var c = getCombinations(5, cards.length);
  var maxRank = 0, winIndex = 10;
  for (i=0; i < c.length; i++) {
       var cs = [cards[c[i][0]], cards[c[i][1]], cards[c[i][2]], cards[c[i][3]], cards[c[i][4]]];
       var ss = [suits[c[i][0]], suits[c[i][1]], suits[c[i][2]], suits[c[i][3]], suits[c[i][4]]];
       index = calcIndex(cs,ss);
       if (handRanks[index] > maxRank) {
           maxRank = handRanks[index];
           winIndex = index; 
           wci = c[i].slice();
           console.log('cs: ' + cs);
       } else if (handRanks[index] == maxRank) {
           //If by chance we have a tie, find the best one
          var other_hand = [cards[wci[0]],cards[wci[1]],cards[wci[2]], cards[wci[3]],cards[wci[4]]];
          // console.log('cs: ' + cs);
          // console.log('other hand: ' + other_hand);
          var score1 = getPokerScore(cs);
          var score2 = getPokerScore(other_hand);
          if (score1 > score2) { wci = c[i].slice(); }
       }
  } 
  return [ winIndex, cards ];
}

function hand(holeCards, board) {
  heroesHand = holeCards.concat(board).join('');
  rankHandReturn = rankHand(heroesHand);
  console.log('return: ' + rankHandReturn[1]);
  var out = {};
  var ranks = [];
  var pairs = rankHandReturn[1].reduce(function(acc, el, i, arr) {
    if (arr.indexOf(el) !== i && acc.indexOf(el) < 0) acc.push(el); return acc;
  }, []);
  console.log('pairs: ' + pairs);
  if (rankHandReturn[0] == 6) {
    console.log('6');
    var filtered = rankHandReturn[1].filter(function(el) {
      return el != pairs[0] && el != pairs[1]
      });
    console.log('filtered: ' + filtered);
  };
  if (rankHandReturn[0] == 5) {
    console.log('5');
    var filtered = rankHandReturn[1].filter(function(el) {
      return el !== rankHandReturn[1].includes(el);
    });
  };
  filtered.sort((a, b) => (a - b)).reverse();
  pairs.sort((a, b) => (a - b)).reverse();
  console.log('filtered: ' + filtered);
  console.log('pairs: ' + pairs);
  // if (rankHandReturn[0] == 8) { var highCards = hand.slice(0, 3); }
  // if (rankHandReturn[0] == 5) { var highCards = hand.slice(0, 4); }
  if (rankHandReturn[0] == 5) { var highCards = pairs.concat(filtered.slice(0, 3)); }
  if (rankHandReturn[0] == 6) { var highCards = pairs.concat(filtered.slice(0, 1)); }
  for (var i=0;i<highCards.length;i++) { 
    ranks.push(cardsLookup[highCards[i]]);
  }
  out['type'] = hands[rankHandReturn[0]];
  out['ranks'] = ranks;
  return out;
}