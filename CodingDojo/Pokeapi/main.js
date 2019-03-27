function pokeSubmit(){
    var param = document.getElementById("pokeInput").value;
    var pokeURL = "http://pokeapi.co/api/v2/pokemon/" + param;

    // new URL for 3rd GET request
    var pokeURL2 = "http://pokeapi.co/api/v2/pokemon/" + param;

    $.getJSON(pokeURL, function(data){
        //console.log(data);
        var pokeID = data.id;
        var pokeName = data.name;
        var pokeType1 = data.types[0].name;
        if (data.types.length == 2) {
            var pokeType2 = data.types[1].name;
        }
        else var pokeType2 = null;
        
        var descriptionURI = "http://pokeapi.co" + data.descriptions[0].resource_uri;
        var pokeDescription = "";

        $.getJSON(descriptionURI, function(data2){
            console.log(data2);
            pokeDescription = data2.description;
        });

        // 3rd GET request to get an image
        $.getJSON(pokeURL2, function(data3){
            // console.log(data3);
            // console.log(JSON.stringify(data, null, "  "));
            var imageURI = data3.sprites.front_default;
            
            console.log("Number: ", pokeID);
            console.log("Name: ", pokeName);
            console.log("Type 1: ", pokeType1);
            console.log("Type 2: ", pokeType2);
            console.log("Description URI: ", descriptionURI);
            console.log("Description: ", pokeDescription);
            
           // append data to HTML
            // empty string to hold HTML
            var li = "";
            li += '<li><img src="' + imageURI + '">';
            li += '<h1>#' + pokeID + ' ' + pokeName + '</h1>';
            li += '<p>Type 1: ' + pokeType1 + '</p>';

            // only display Type 2 if it is not null
            if (pokeType2 != null){
                li += '<p>Type 2: ' + pokeType2 + '</p>';
            }

            li += '<p>' + pokeDescription + '</p>';
            li += '</li>';

            // empty the listview
            $("#pokeDetails").empty();

            // append new li to listview
            $("#pokeDetails").append(li).promise().done(function(){
                    $(this).listview("refresh");
            });
        });

    });	// 2nd and 3rd GET requests are nested in success function of 1st GET request
}