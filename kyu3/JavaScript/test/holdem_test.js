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

});
