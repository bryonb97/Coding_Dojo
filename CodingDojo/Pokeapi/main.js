$(function () {
    // alert("Ready!");

    //#region API URL Calls
    // URLS for the API 
    // Main URL for GET request
    var pokeURL = "http://pokeapi.co/api/v2/pokemon/";

    // new URL for 2nd GET request to get characteristics 
    // Not working right now
    // Needed for sprite though
    var pokeURLCharacteristics = "http://pokeapi.co/api/v2/characteristic/";

    // New URL for 3rd GET request to get Abilities and Moves
    var pokeURLAbility = "https://pokeapi.co/api/v2/pokemon/";
    //#endregion 

    $(".searchBtn").click(pokeURL, function (pokeSubmit) {
        var param = document.getElementById("pokeInput").value;
        var lowercase = param.toLowerCase();
        document.getElementById("pokeInput").value = lowercase;
        param = lowercase;
        // console.log(param);

        //#region Add Parameter to URLS
        pokeURL = "http://pokeapi.co/api/v2/pokemon/" + param;
        pokeURLCharacteristics = "http://pokeapi.co/api/v2/characteristic/";
        pokeURLAbility = "https://pokeapi.co/api/v2/pokemon/" + param;
        //#endregion
        var $pokeDetails = $("#pokeDetails");

        //#region GET Requests
        $.ajax({
            url: pokeURL,
            success: function (dataID) {
                var pokeID = dataID.id;
                var pokeName = dataID.name;
                var pokeOrder = dataID.order;
                var pokeType1 = dataID.types[0].type.name;

                if (dataID.types.length == 2) {
                    var pokeType2 = dataID.types[1].type.name;
                } else var pokeType2 = null;

                var pokeDescription = "";

                $.ajax({
                    url: pokeURLCharacteristics,
                    success: function (dataSprites) {
                        var imageURI = dataID.sprites.front_default;


                        $.ajax({
                            url: pokeURLAbility,
                            success: function (dataAbility) {
                                var pokeWeight = dataAbility.weight;
                                var pokeHeight = dataAbility.height;
                                var abilityName = dataAbility.abilities.ability;
                                var mainAbility = dataAbility.abilities[0].ability.name;
                                var moves = dataAbility.moves[0].move.name;

                                for (var i = 0; i < dataAbility.moves.length; i++) {
                                    moves = dataAbility.moves[i].move.name;
                                    // console.log("Move " + i + ": " + moves);
                                }

                                // append data to HTML
                                // empty string to hold HTML
                                var li = "";
                                li += '<li id="pokeImg"><img src="' + imageURI + '"></li>';
                                li += '<h1 id="pokeID">#' + pokeID + ' ' + pokeName + '</h1>';
                                li += '<h2 id="pokeOrder">' + 'Order: ' + pokeOrder + '</h2>';

                                li += '<p id="pokeType">Type 1: ' + pokeType1 + '</p>';

                                // only display Type 2 if it is not null
                                if (pokeType2 != null) {
                                    li += '<p id="pokeType">Type 2: ' + pokeType2 + '</p>';
                                }

                                li += '<h1 id="mainAbility">' + mainAbility + '</h1>';



                                li += '<input type="button" class="btnDark" id="showMovesBtn" onclick="showMoves();" value="Show Moves">';

                                for (var i = 0; i < dataAbility.moves.length; i++) {
                                    moves = dataAbility.moves[i].move.name;
                                    li += '<p class="movesList">' + "Move " + [i + 1] + ": " + moves + '</p>';
                                    // console.log(i);
                                }

                                li += '<p>' + pokeDescription + '</p>';
                                li += '</li>';

                                // empty the listview
                                $("#pokeDetails").empty();

                                // append new li to listview
                                $("#pokeDetails").append(li);



                            }
                        })
                    }
                })
                //2nd and 3rd GET requests are nested in success function of 1st GET request
                //#endregion 
                $("#showMovesBtn").click(function () {
                    // alert("Button Clicked!");
                });
            }
        })
    });
});

function showMoves() {
    // console.log("Showing moves");
    $(".movesList").slideToggle("slow");
}