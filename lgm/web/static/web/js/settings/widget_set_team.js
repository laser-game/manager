// spočítá kolik hráčů má jakou barvu a zobrazí tuto informaci
function ColorCounter() {
    var Members = 0;
    for (i = 0; i < Color.length; i++) {
        Color[i].Members = 0;
    }
    for (i = 0; i < Player.length; i++) {
        if (Player[i].Available) {
            Color[Player[i].Color].Members++;
            Members++;
        }
    }
    for (i = 1; i < Color.length; i++) {
        $("#color-members-" + i.toString()).text(Color[i].Members);
    }
    $("#color-members-all").text(Members);
}

// získá informace o týmech
function GetTeam() {
    for (i = 0; i < Color.length - 1; i++) {
        Team[i].ID = i;
        Team[i].Name = $("#team-name-" + (i + 1).toString()).val();
        Team[i].Color = i + 1;
        for (j = 0; j < Player.length; j++) {
            if (Player[j].Available && Player[j].Color == Team[i].Color) {
                Team[i].Available = true;
            }
        }
    }
}

$(document).ready(function () {
    // click na color erb nebo color lock
    $(".color-erb, .color-lock").click(function () {
        var id = parseInt($(this).attr("id").split("-")[2]);
        Color[id].Available = !Color[id].Available;
        $("#team-name-" + id.toString()).prop("disabled", !Color[id].Available);
        $("#color-lock-" + id.toString()).toggle(100);
    });
});
