// spočítá kolik hráčů má jakou barvu a zobrazí tuto informaci
function ColorCounter() {
    var members = 0;
    for (i = 0; i < Color.length; i++) {
        Color[i].members = 0;
    }
    for (i = 0; i < Player.length; i++) {
        if (Player[i].anable) {
            Color[Player[i].color_index].members++;
            members++;
        }
    }
    for (i = 0; i < Color.length; i++) {
        $("#color-members-" + i.toString()).text(Color[i].members);
    }
    $("#color-members-all").text(members);
}

// získá informace o týmech
function GetTeam() {
    for (i = 0; i < Color.length; i++) {
        Team[i].id = i;
        Team[i].name = $("#team-name-" + i.toString()).val();
        Team[i].color_index = i;
        for (j = 0; j < Player.length; j++) {
            if (Player[j].anable && Player[j].color_index == Team[i].color_index) {
                Team[i].anable = true;
            }
        }
    }
}

$(document).ready(function () {
    // click na color erb nebo color lock
    $(".color-erb, .color-lock").click(function () {
        var id = parseInt($(this).attr("id").split("-")[2]);
        Color[id].anable = !Color[id].anable;
        $("#team-name-" + id.toString()).prop("disabled", !Color[id].anable);
        $("#color-lock-" + id.toString()).toggle(100);
    });
});
