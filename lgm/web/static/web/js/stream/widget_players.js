// načteme informace hráčích
function GetActualPlayers() {
    $.getJSON("/api/actual-players", function (Players) {

        HTML_code = '<tr>';
        HTML_code += '<th> POŘADÍ </th>';
        HTML_code += '<th> JMÉNO </th>';
        HTML_code += '<th> ZABITÍ </th>';
        HTML_code += '<th> ÚMRTÍ </th>';
        HTML_code += '<th> SKÓRE </th>';
        HTML_code += '</tr>';

        for (i in Players) {
            Player = Players[i]
            HTML_code += '<tr>';

            HTML_code += '<td align="center">';
            HTML_code += Player.position;
            HTML_code += '</td>';

            HTML_code += '<td align="center">';
            HTML_code += '<span style="color: ' + Player.color + '; font-weight: 400;">' + Player.name + '</span>' + '<br>';
            HTML_code += '</td>';

            HTML_code += '<td align="center">';
            HTML_code += Player.kills_count;
            HTML_code += '</td>';

            HTML_code += '<td align="center">';
            HTML_code += Player.deaths_count;
            HTML_code += '</td>';

            HTML_code += '<td align="center">';
            HTML_code += Player.points;
            HTML_code += '</td>';

            HTML_code += '</tr>';
        }
        $("#state-players").html(HTML_code);
        setTimeout(GetActualPlayers, 1000);
    });
}

$(document).ready(function () {
    GetActualPlayers();
});
