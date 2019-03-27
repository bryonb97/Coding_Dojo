function rollDie(sides) {
    return Math.floor(Math.random() * sides) + 1;
}
// rollDie(21);

function playStats(rolls, sides = 6) {
    var sum = 0;
    var min = 6;
    var max = 1;
    var avg = 0;

    for (var i = 0; i < rolls; i++) {
        var roll = rollDie(sides);
        sum += roll;
        if (roll > max) {
            max = roll;
        }
        if (roll < min) {
            min = roll;
        }
    }
    avg = Math.trunc(sum / rolls);
    var results = "Min:" + min + " Max:" + max + " Avg:" +
        avg + " Sum:" + sum;
    return results;
}
// console.log(playStats(5, 10));
