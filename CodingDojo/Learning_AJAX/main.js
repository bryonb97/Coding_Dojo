$(function(){

    $.ajax({
        type: "GET",
        url: "",
        data: "data",
        success: function (response) {
            alert("Success!");
        
            $("#changeMe").css("background-color", "red");
                
            
        }
    });

    


});
    