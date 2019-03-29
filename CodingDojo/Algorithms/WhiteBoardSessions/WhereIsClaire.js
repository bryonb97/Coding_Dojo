var claire = [0, 0];

function xLocation() {
    return claire[0];
}

function yLocation() {
    return claire[1];
}

function reset() {
    claire = [0, 0];
}

function moveBy(x, y) {
    claire[0] = xLocation() + x;
    claire[1] = yLocation() + y;
    console.log(x, y);
}
moveBy(23, 43)

function distanceFromHome() {
    var x = 0;
    var y = 0;

    if (claire[0] < 0) {
        x = claire[0] * -1;
    } else {
        x = claire[0];
    }

    if (claire[1] < 0) {
        y = claire[1] * -1;
    } else {
        y = claire[1];
    }

    var string = 'X:' + x + ' Y:' + y;
    return string;
}
distanceFromHome();