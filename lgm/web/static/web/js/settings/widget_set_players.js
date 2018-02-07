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

$(document).ready(function () {
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
