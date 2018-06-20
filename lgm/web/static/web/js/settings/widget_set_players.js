function PlayerGet() {
    for (i = 0; i < Player.length; i++) {
        Player[i].name = $("#player-name-" + i.toString()).val();
    }
}

function PlayerSet() {
    for (i = 0; i < Player.length; i++) {
        $("#player-name-" + i.toString()).val(Player[i].name);
        $("#player-name-" + i.toString()).prop("disabled", !Player[i].enable);
        if (Player[i].enable) {
            var code = "";
            code += '<svg viewBox="0 -7 90 107" style="height: 0.8em; fill: ' + Color[Player[i].color_index].rgb + ';">';
            code += '<polygon points="0,0 90,0 85,80 45,100 5,80"/></svg>';

            $("#player-erb-" + i.toString()).html(code);
        }
        else {
            $("#player-erb-" + i.toString()).html('<img src="/static/web/img/lock.svg" style="height: 0.8em;">');
        }
    }
}

$(document).ready(function () {
    // nastavení barev
    $(".player-erb").click(function () {
        PlayerGet();
        var id = parseInt($(this).attr("id").split("-")[2]);
        var color_is_enable = false;

        for (i = Player[id].color_index + 1; i < Color.length; i++) {
            if (Color[i].enable) {
                Player[id].color_index = i;
                Player[id].enable = true;
                color_is_enable = true;
                break;
            }
        }

        if (!color_is_enable) {
            Player[id].color_index = -1;
            Player[id].enable = false;
        }

        PlayerSet();
        ColorCounter();
    });
});
