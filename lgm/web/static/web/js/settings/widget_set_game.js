var SetGame;
var GameTypes = [];
// načteme informace o možných typech her
function GetGameTypes() {
    $.getJSON("/game-types", function (data) {
        for (i = 0; i < data.length; i++) {
            GameTypes[i] = data[i];
        }
        SetGameTypes();
        SetGameDefault();
    });

}

// nastaví jména her
function SetGameTypes() {
    var code = "";
    for (i = 0; i < GameTypes.length; i++) {
        code += '<option  value="' + i + '">' + GameTypes[i].Name + '</option>';
    }
    $("#SetGame-Name").html(code);
}

// nastaví výchozí konfigurace her
function SetGameDefault() {
    var id = $("#SetGame-Name").val();
    SetGame = JSON.parse(JSON.stringify(GameTypes[id]));
    SetGame.Name = GameTypes[id].Name;

    $("#SetGame-GameTime").val(SetGame.GameTime);
    $("#SetGame-DeathTime").val(SetGame.DeathTime);
    $("#SetGame-ShotsInBatch").val(SetGame.ShotsInBatch);

    SetCheckBox("#SetGame-Sound", SetGame.Sound);
    SetCheckBox("#SetGame-Immorality", SetGame.Immorality);
    SetCheckBox("#SetGame-OffLED", SetGame.OffLED);

    SetRadio("SetGame-Fn", SetGame.Fn);
}

// načtení nastavení hry
function GetGameSettings() {
    SetGame.GameTime = parseInt($("#SetGame-GameTime").val());
    SetGame.DeathTime = parseInt($("#SetGame-DeathTime").val());
    SetGame.ShotsInBatch = parseInt($("#SetGame-ShotsInBatch").val());
}

$(document).ready(function () {
    // checkbox nastavení hry
    $("#SetGame-Sound").click(function () {
        SetGame.Sound = !SetGame.Sound;
        SetCheckBox(this, SetGame.Sound);
    });
    $("#SetGame-Immorality").click(function () {
        SetGame.Immorality = !SetGame.Immorality;
        SetCheckBox(this, SetGame.Immorality);
    });
    $("#SetGame-OffLED").click(function () {
        SetGame.OffLED = !SetGame.OffLED;
        SetCheckBox(this, SetGame.OffLED);
    });

    // Fn radio click
    $(".SetGame-Fn").click(function () {
        var id = parseInt($(this).attr("id").split("-")[2]);
        SetGame.Fn = id;
        SetRadio("SetGame-Fn", SetGame.Fn);
    });
});
