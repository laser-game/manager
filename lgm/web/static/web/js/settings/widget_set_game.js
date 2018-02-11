var SetGame;
var GameTypes = [];
// načteme informace o možných typech her
function GetGameTypes() {
    $.getJSON("/api/type-game", function (data) {
        for (i = 0; i < data.length; i++) {
            GameTypes = data;
        }
        SetGameTypes();
        SetGameDefault();
    });

}

// nastaví jména her
function SetGameTypes() {
    var code = "";
    for (i = 0; i < GameTypes.length; i++) {
        code += '<option  value="' + i + '">' + GameTypes[i].name + '</option>';
    }
    $("#SetGame-Name").html(code);
}

// nastaví výchozí konfigurace her
function SetGameDefault() {
    var id = $("#SetGame-Name").val();
    SetGame = JSON.parse(JSON.stringify(GameTypes[id]));
    SetGame.name = GameTypes[id].name;

    $("#SetGame-GameTime").val(SetGame.game_duration / 60);
    $("#SetGame-DeathTime").val(SetGame.death_duration);
    $("#SetGame-ShotsInBatch").val(SetGame.batch_shots_count);

    Check.set("SetGame-Sound", SetGame.enable_sound);
    Check.set("SetGame-Immorality", SetGame.enable_immorality);
    Check.set("SetGame-OffLED", !SetGame.enable_vest_light);

    var fn;
    switch(SetGame.button_action_mode) {
    case 'F':
        fn = 0;
        break;
    case 'W':
        fn = 1;
        break;
    case 'U':
        fn = 2;
        break;
    default:
        fn = 3;
    }
    Radio.set("Fn", fn);

    var game_mode;
    switch(SetGame.game_mode) {
    case 'S':
        game_mode = 0;
        break;
    default:
        game_mode = 1;
    }
    Radio.set("GameType", game_mode);
}

// načtení nastavení hry
function GetGameSettings() {
    SetGame.game_duration = 60 * parseInt($("#SetGame-GameTime").val());
    SetGame.death_duration = parseInt($("#SetGame-DeathTime").val());
    SetGame.batch_shots_count = parseInt($("#SetGame-ShotsInBatch").val());
}

$(document).ready(function () {
    $('*').click(function () {
        SetGame.enable_sound = Check.get('SetGame-Sound')
        SetGame.enable_immorality = !Check.get('SetGame-Immorality')
        SetGame.enable_vest_light = !Check.get('SetGame-OffLED')

        var fn;
        switch(Radio.get('Fn')) {
        case 0:
            fn = 'F';
            break;
        case 1:
            fn = 'W';
            break;
        case 2:
            fn = 'U';
            break;
        default:
            fn = 'D';
        }
        SetGame.button_action_mode = fn;

        var game_mode;
        switch(Radio.get("GameType")) {
        case 0:
            game_mode = 'S';
            break;
        default:
            game_mode = 'T';
        }
        SetGame.game_mode = game_mode;
    });
});
