$(document).ready(function () {
  $(".text").textillate({
    loop: true,
    speed: 1500,
    sync: true,
    in: {
      effect: "bounceIn",
    },
    out: {
      effect: "bounceOut",
    },
  });
  $(".siri-message").textillate({
    loop: true,
    speed: 1500,
    sync: true,
    in: {
      effect: "fadeInUp",
      sync: true,
    },
    out: {
      effect: "fadeOutDown",
      sync: true,
    },
  });

  //   var siriWave = new SiriWave({
  //     container: document.getElementById("siri-container"),
  //     width: 940,
  //     // style: "ios9",
  //     amplitude: 1,
  //     height: 200,
  //     speed: 0.3,
  //     autostart: true,
  //     waveColor: "#ff0000",
  //     waveOffset: 0,
  //     rippleEffect: true,
  //     rippleColor: "#ffffff",
  //   });
  //   siriWave.start();

  $("#MicBtn").click(function (e) {
    e.preventDefault();
    if (typeof eel !== "undefined") {
      eel.playAssistantSound();
    } else {
      console.log("Eel is not defined");
    }
    $("#Oval").attr("hidden", true);
    $("#SriWave").removeAttr("hidden");
    eel.takeCommand()();
  });
});

// "#00aaff" is the wave color
