function PlayerGet() {
    for (i = 0; i < Player.length; i++) {
        Player[i].Name = $("#player-name-" + (i + 1).toString()).val();
    }
}

function PlayerSet() {
    for (i = 0; i < Player.length; i++) {
        $("#player-name-" + (i + 1).toString()).val(Player[i].Name);
        $("#player-name-" + (i + 1).toString()).prop("disabled", !Player[i].Available);
        if (Player[i].Color) {
            var code = "";
            code += '<svg viewBox="0 -7 90 107" style="height: 0.8em; fill: ' + Color[Player[i].Color].RGB + ';">';
            code += '<polygon points="0,0 90,0 85,80 45,100 5,80"/></svg>';

            $("#player-erb-" + (i + 1).toString()).html(code);
        }
        else {
            $("#player-erb-" + (i + 1).toString()).html('<img src="/static/web/img/lock.svg" style="height: 0.8em;">');
        }
    }
}

function PlayerCreate() {
    var line = '';
    for (i=1; i<=DEFAULT.MAX_PLAYERS; i++) {
        line +=        '<tr>';
        line +=            '<td align="right" class="number">' + i + '</td>';
        line +=            '<td align="center" style="width: 3em;">';
        line +=                '<button class="player-erb" id="player-erb-' + i + '"></button>';
        line +=            '</td>';
        line +=            '<td align="center"><input type="text" class="player-name" id="player-name-' + i + '" value="Player' + i + '"></td>';
        line +=            '<td align="right"><span class="number" id="player-bat-' + i + '">100%</span></td>';
        line +=        '</tr>';
    };
    $('#player-table').html(line);
}

$(document).ready(function () {
    PlayerCreate();
    // nastavení barev
    $(".player-erb").click(function () {
        PlayerGet();
        var id = parseInt($(this).attr("id").split("-")[2]) - 1;

        for (i = Player[id].Color + 1; i < Color.length; i++) {
            if (Color[i].Available && i) {
                Player[id].Color = i;
                Player[id].Available = true;
                break;
            }
        }

        if (i == Color.length) {
            Player[id].Color = 0;
            Player[id].Available = false;
        }

        PlayerSet();
        ColorCounter();
    });
});
