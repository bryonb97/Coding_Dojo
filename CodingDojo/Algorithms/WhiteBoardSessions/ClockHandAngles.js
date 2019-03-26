function clockHandAngles(sec) {
    //Number of seconds in each.
    const DAY = 86400;
    const HOUR = 3600;
    const MIN = 60

    var day = 0;
    var hour = 0;
    var min = 0;

    day = Math.floor(sec / DAY);
    sec -= day * DAY;
    // console.log(day);
    // console.log(sec);

    if (sec >= HOUR) {
        hour = Math.floor(sec / HOUR);
        // console.log("H: " + hour);
        sec -= hour * HOUR;
    }
    if (sec >= MIN) {
        min = Math.floor(sec / MIN);
        // console.log("M: " + min);
        sec -= min * MIN;
    }
    console.log("D: " + day * 51 + " degrees");
    console.log("H: " + hour * 30 + " degrees");
    console.log("M: " + min * 6 + " degrees");
    console.log("S: " + sec * 6 + " degrees");

}
clockHandAngles(119730);