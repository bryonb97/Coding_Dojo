function weekDayName(day) {
    if (day > 7) {
        day = day % 7 + 1
    }
    switch (day) {
        case 1:
            return "Sunday";
        case 2:
            return "Monday";
        case 3:
            return "Tuesday";
        case 4:
            return "Wednesday";
        case 5:
            return "Thursday";
        case 6:
            return "Friday";
        case 7:
            return "Saturday";
        default:
            return "Out of Range";
    }
}
console.log(weekDayName(35));