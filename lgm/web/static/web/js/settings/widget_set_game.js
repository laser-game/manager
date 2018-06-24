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

    switch(SetGame.button_action_mode) {
    case 'F':
        Radio.set("Fn", 0);
        break;
    case 'W':
        Radio.set("Fn", 1);
        break;
    case 'U':
        Radio.set("Fn", 2);
        break;
    default:
        Radio.set("Fn", 3);
    }

    switch(SetGame.game_mode) {
    case 'S':
        Radio.set("GameType", 0);
        break;
    default:
        Radio.set("GameType", 1);
    }

    switch(SetGame.sound_set_type) {
    case 'CZ':
        Radio.set("SoundSetType", 0);
        break;
    default:
        Radio.set("SoundSetType", 1);
    }
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
        SetGame.enable_immorality = Check.get('SetGame-Immorality')
        SetGame.enable_vest_light = !Check.get('SetGame-OffLED')

        switch(Radio.get('Fn')) {
        case 0:
            SetGame.button_action_mode = 'F';
            break;
        case 1:
            SetGame.button_action_mode = 'W';
            break;
        case 2:
            SetGame.button_action_mode = 'U';
            break;
        default:
            SetGame.button_action_mode = 'D';
        }

        switch(Radio.get("GameType")) {
        case 0:
            SetGame.game_mode = 'S';
            break;
        default:
            SetGame.game_mode = 'T';
        }

        switch(Radio.get('SoundSetType')) {
        case 0:
            SetGame.sound_set_type = 'CZ';
            break;
        default:
            SetGame.sound_set_type = 'EN';
        }
    });
});
