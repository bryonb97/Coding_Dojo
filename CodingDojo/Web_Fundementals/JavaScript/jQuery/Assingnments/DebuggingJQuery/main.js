$(document).ready(function () {
    // alert("READY!");

    $('p, h3, li').hover(function (e) {
        $(this).css("color", e.type === "mouseenter" ? "white" : "black");

    });

    $('a').click(function () {
        alert("we don't actually serve pizza...");
    });

    $('img').click(function () {
        $(this).slideUp();
    });

    $('h5').click(function () {
        $('img').slideDown();
    });

    $('#submitBtn').click(function () {
        var result = $('input[name=topping]:checked').val();
        alert("Thank you for your input, we like " + result + " too!");
    });
});