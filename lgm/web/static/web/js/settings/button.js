$(document).ready(function () {

    // click na typ hry nebo tlačítko obnovit
    $("#SetGame-Name, #refresh").click(function () {
        SetGameDefault();
    });

    // clicknutí na tlačítko vyčistit
    $("#clear").click(function () {
        for (i = 0; i < Player.length; i++) {
            Player[i].Name = "";
            Player[i].Color = 0;
            Player[i].Available = false;
        }
        PlayerSet();
        ColorCounter();
    });

    // zapnout všechny vesty
    $("#turn-vests").click(function () {
        PlayerGet();

        var ColorReady = 0;
        for (i = 1; i < Color.length; i++) {
            if (Color[i].Available) {
                ColorReady = i;
                break;
            }

        }
        if (ColorReady) {
            for (i = 0; i < Player.length; i++) {
                if (Player[i].Name == "") {
                    Player[i].Name = "Player" + (i + 1).toString();
                }
                Player[i].Color = ColorReady;
                Player[i].Available = true;
            }
        }

        PlayerSet();
        ColorCounter();
    });

    // rozdělení teamů
    $("#split").click(function () {
        var PlayerReady = [];
        var ColorReady = [];

        for (i = 0; i < Player.length; i++) {
            if (Player[i].Available) {
                PlayerReady.push(i);
            }
        }

        for (i = 1; i < Color.length; i++) {
            if (Color[i].Available) {
                ColorReady.push(i);
            }
        }

        // pokud není vybrána žádná barva nebo žádný hráč
        if (ColorReady.length == 0 || PlayerReady.length == 0) {
            for (i = 0; i < Player.length; i++) {
                Player[i].Color = 0;
            }
        }
        // vytvořme teamy
        else {
            var TeamMembers = parseInt(PlayerReady.length / ColorReady.length);
            if (ColorReady.length > PlayerReady.length) {
                TeamMembers = 1;
            }

            for (i = 0, c = 0; i < PlayerReady.length; i++) {
                Player[PlayerReady[i]].Color = ColorReady[c];
                if ((i + 1) % TeamMembers == 0 && c + 1 < ColorReady.length) {
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
            url: '/game-config',
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
        config.Play = true;

        $.ajax({
            type: 'POST',
            url: '/game-cmd',
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
        config.Play = false;

        $.ajax({
            type: 'POST',
            url: '/game-cmd',
            data: JSON.stringify(config),
            success: function (data) {
                console.log(data.state);
            },
            contentType: "application/json",
            dataType: 'json'
        });
    });

});