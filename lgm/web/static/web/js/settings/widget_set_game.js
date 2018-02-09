var SetGame;
var GameTypes = [];
// načteme informace o možných typech her
function GetGameTypes() {
    $.getJSON("/api/game-types", function (data) {
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

    SetCheckBox("SetGame-Sound", SetGame.Sound);
    SetCheckBox("SetGame-Immorality", SetGame.Immorality);
    SetCheckBox("SetGame-OffLED", SetGame.OffLED);

    SetRadio("Fn", SetGame.Fn);
}

// načtení nastavení hry
function GetGameSettings() {
    SetGame.GameTime = parseInt($("#SetGame-GameTime").val());
    SetGame.DeathTime = parseInt($("#SetGame-DeathTime").val());
    SetGame.ShotsInBatch = parseInt($("#SetGame-ShotsInBatch").val());
}

$(document).ready(function () {
    $('*').click(function () {
        SetGame.Sound = GetCheckBox('SetGame-Sound')
        SetGame.Immorality = GetCheckBox('SetGame-Immorality')
        SetGame.OffLED = GetCheckBox('SetGame-OffLED')
        SetGame.Fn = GetRadio('Fn');
    });
});
