suite('holdem_tests', function() {

    test('getCards returns array of card values', function() {
        expect(getCards('A♦A♣5♥5♣K♥Q♥K♦')).to.deep.equal([ '14', '14', '5', '5', '13' ,'12', '13' ]);
    });

    test('getSuits returns an array of suits', function() {
        expect(getSuits('A♦A♣5♥5♣K♥Q♥K♦')).to.deep.equal([ '♦', '♣', '♥', '♣', '♥', '♥', '♦' ]);
    });

    test('getCombinations returns an array of correct size', function() {
        var c = getCombinations(5, 7);
        expect(c.length).to.equal(21);
    });

    test('getPokerScore returns correct integer score for given hand', function() {
        expect(getPokerScore([14,14,5,5,12])).to.equal(976220);
    });

    test('rankHand returns correct index to lookup hand value for 2pair', function(){
        expect(rankHand('A♦A♣5♥5♣K♥Q♥K♦')).to.equal(6);
    });

    test('rankHand returns correct index to lookup hand value for 4 of a kind', function(){
        expect(rankHand('A♦A♣A♥A♠5♣K♥Q♥')).to.equal(0);
    });

    test('rankHand returns correct index to lookup hand value for a flush', function(){
        expect(rankHand('A♠K♦J♥5♥10♥Q♥3♥')).to.equal(3);
    });

    test('hand returns string nothing for high card hand', function() {
        hero = hand(['K♠','A♦'],['J♣','Q♥','9♥','2♥','3♦']);
        expect(hero.type).to.equal('nothing');
        expect(hero.ranks).to.deep.equal(['A','K','Q','J','9']);
    });

    test('hand returns string pair', function() {
        hero = hand(['K♠','Q♦'],['J♣','Q♥','9♥','2♥','3♦']);
        expect(hero.type).to.equal('pair');
        expect(hero.ranks).to.deep.equal(['Q','K','J','9']);
    });

    test('hand returns string two pair', function() {
        hero = hand(['K♠','J♦'],['J♣','K♥','9♥','2♥','3♦']);
        expect(hero.type).to.equal('two pair');
        expect(hero.ranks).to.deep.equal(['K','J','9']);
    });

    test('hand returns string three-of-a-kind', function() {
        hero = hand(['4♠','9♦'],['J♣','Q♥','Q♠','2♥','Q♦']);
        expect(hero.type).to.equal('three-of-a-kind');
        expect(hero.ranks).to.deep.equal(['Q','J','9']);
    });

    test('hand returns string straight-flush', function() {
        hero = hand(['8♠','6♠'],['7♠','5♠','9♠','J♠','10♠']);
        expect(hero.type).to.equal('straight-flush');
        expect(hero.ranks).to.deep.equal(['J','10','9','8','7']);
    });
    
});
