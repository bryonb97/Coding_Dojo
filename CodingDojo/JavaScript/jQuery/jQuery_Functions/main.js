// A $( document ).ready() block.
$(document).ready(function () {
    // alert("I'm an alert!");


    function initialize() {
        // Update the controls on load
        // updateTimerDisplay();
        // updateProgressBar();

        // Clear any old interval.
        clearInterval(time_update_interval);

        // Start interval to update elapsed time display and
        // the elapsed part of the progress bar every second.
        // time_update_interval = setInterval(function () {
        //     updateTimerDisplay();
        //     updateProgressBar();
        // }, 1000)
    }

    var player;

    function onYouTubeIframeAPIReady() {
        player = new YT.Player('hidden', {
            width: 600,
            height: 400,
            videoId: '1QCMsh2henc',
            playerVars: {
                'autoplay' : 1,
                'start': 3,
                'showInfo': 0,
                'modestbranding': 0,
                'loop': 0,
                'fs': 0,
                'cc_load_policty': 0,
                'iv_load_policy': 3
            },
            events: {
                'onReady': function (e) {
                    // e.target.mute();
                    e.target.setVolume(100);      // YOU CAN SET VALUE TO 100 FOR MAX VOLUME.
                }
            }
        });
    }




    clicked = true;
    $("#addClassBtn").click(function () {
        
        if (clicked) {
            $("#addClassContainer p").last().addClass("red");
            clicked = false;
        } else {
            $("#addClassContainer p").last().removeClass("red");
            clicked = true;
        }
    });

    $("#slidetoggleBtn").click(function(){
        console.log("Open video");
        $("#hidden").show().slideToggle("slow", onYouTubeIframeAPIReady());
    });
        
    $("#appendBtn").click(function () {
        $("#append").append("Ahhhhhhhhh");
    });
});