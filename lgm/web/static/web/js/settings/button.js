$(document).ready(function () {

    // click na typ hry nebo tlačítko obnovit
    $("#SetGame-Name, #refresh").click(function () {
        SetGameDefault();
    });

    // clicknutí na tlačítko vyčistit
    $("#clear").click(function () {
        for (i = 0; i < Player.length; i++) {
            Player[i].name = "";
            Player[i].color_index = 0;
            Player[i].enable = false;
        }
        PlayerSet();
        ColorCounter();
    });

    // zapnout všechny vesty
    $("#turn-vests").click(function () {
        PlayerGet();

        var color_ready = 0;
        var color_is_enable = false;
        for (i = 0; i < Color.length; i++) {
            if (Color[i].enable) {
                color_ready = i;
                color_is_enable = true;
                break;
            }

        }
        if (color_is_enable) {
            for (i = 0; i < Player.length; i++) {
                if (Player[i].name == "") {
                    Player[i].name = "Player" + (i + 1).toString();
                }
                Player[i].color_index = color_ready;
                Player[i].enable = true;
            }
        }

        PlayerSet();
        ColorCounter();
    });

    // rozdělení teamů
    $("#split").click(function () {
        var player_ready = [];
        var color_ready = [];

        for (i = 0; i < Player.length; i++) {
            if (Player[i].enable) {
                player_ready.push(i);
            }
        }

        for (i = 0; i < Color.length; i++) {
            if (Color[i].enable) {
                color_ready.push(i);
            }
        }

        // pokud není vybrána žádná barva nebo žádný hráč
        if (color_ready.length == 0 || player_ready.length == 0) {
            for (i = 0; i < Player.length; i++) {
                Player[i].enable = false;
            }
        }
        // vytvořme teamy
        else {
            var TeamMembers = parseInt(player_ready.length / color_ready.length);
            if (color_ready.length > player_ready.length) {
                TeamMembers = 1;
            }

            for (i = 0, c = 0; i < player_ready.length; i++) {
                Player[player_ready[i]].color_index = color_ready[c];
                if ((i + 1) % TeamMembers == 0 && c + 1 < color_ready.length) {
                    ++c;
                }
            }
        }
        PlayerSet();
        ColorCounter();
    });

    // nastavení vest
    $("#set-vests").click(function () {
        GetGameSettings();
        PlayerGet();
        GetTeam();

        var config = Object();
        config.SetGame = SetGame;
        config.Player = Player;
        config.Team = Team;

        $.ajax({
            type: 'POST',
            url: '/api/game-config',
            data: JSON.stringify(config),
            success: function (data) {
                console.log(data.state);
            },
            contentType: "application/json",
            dataType: 'json'
        });
    });

    // start hry
    $("#start-game").click(function () {
        config = Object();
        config.play = true;

        $.ajax({
            type: 'POST',
            url: '/api/game-cmd',
            data: JSON.stringify(config),
            success: function (data) {
                console.log(data.state);
            },
            contentType: "application/json",
            dataType: 'json'
        });
    });

    // konec hry
    $("#end-game").click(function () {
        config = Object();
        config.play = false;

        $.ajax({
            type: 'POST',
            url: '/api/game-cmd',
            data: JSON.stringify(config),
            success: function (data) {
                console.log(data.state);
            },
            contentType: "application/json",
            dataType: 'json'
        });
    });

});
