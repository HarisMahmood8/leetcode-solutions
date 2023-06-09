/**
 * @param {character[]} letters
 * @param {character} target
 * @return {character}
 */
var nextGreatestLetter = function(letters, target) {
    let count = 0;
    for(var i = 0; i < letters.length; i++) {
        if (letters[i] > target) {
            return letters[i];
        }
        else {
            count += 1;
        }


    }
    if(count == letters.length) {
        return letters[0];
    }
 }
