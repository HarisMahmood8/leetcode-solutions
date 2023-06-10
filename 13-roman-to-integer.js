/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    var map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D":500, "M":1000};
    var val = 0;
    for(var i = 0; i < s.length; i++) {
        //val += map[s[i]];
        if(i+1 > s.length) {
            val = val + map[s[i]];
        }
        else if(map[s[i]] < map[s[i+1]]) {
            val = val - map[s[i]];
        }
        else {
            val += map[s[i]];
        }
    }
    return val;
}
