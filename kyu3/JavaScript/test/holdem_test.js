suite('holdem_tests', function() {
    
        test('getCardStr returns cardStr with replaced broadway cards', function() {
            expect(GetCardStr('A♦A♣5♥5♣K♥Q♥K♦')).to.equal(14,14,5,5,13,12,13);
        });
    });