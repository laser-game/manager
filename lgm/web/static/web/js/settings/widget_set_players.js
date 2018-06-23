function PlayerGet() {
    for (i = 0; i < Player.length; i++) {
        Player[i].name = $("#player-name-" + Player[i].address).val();
    }
}

function PlayerSet() {
    for (i = 0; i < Player.length; i++) {
        $("#player-name-" + Player[i].address).val(Player[i].name);
        $("#player-name-" + Player[i].address).prop("disabled", !Player[i].enable);
        if (Player[i].enable) {
            var code = "";
            code += '<svg viewBox="0 -7 90 107" style="height: 0.8em; fill: ' + Color[Player[i].color_index].rgb + ';">';
            code += '<polygon points="0,0 90,0 85,80 45,100 5,80"/></svg>';

            $("#player-erb-" + Player[i].address).html(code);
        }
        else {
            $("#player-erb-" + Player[i].address).html('<img src="/static/web/img/lock.svg" style="height: 0.8em;">');
        }
    }
}

function player_address_to_index(address) {
    for (index = 0; index < Player.length; index++)
    {
        if (Player[index].address == address) {
            break;
        }
    }
    return index;
}

$(document).ready(function () {
    // nastavení barev
    $(".player-erb").click(function () {
        PlayerGet();
        var id = parseInt($(this).attr("id").split("-")[2]);
        var index = player_address_to_index(id);
        var color_is_enable = false;



        for (i = Player[index].color_index + 1; i < Color.length; i++) {
            if (Color[i].enable) {
                Player[index].color_index = i;
                Player[index].enable = true;
                color_is_enable = true;
                break;
            }
        }

        if (!color_is_enable) {
            Player[index].color_index = -1;
            Player[index].enable = false;
        }

        PlayerSet();
        ColorCounter();
    });
});
