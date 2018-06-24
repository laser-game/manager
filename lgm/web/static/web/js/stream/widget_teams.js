// načteme informace týmech
function GetActualTeam() {
    $.getJSON("/api/actual-teams", function (Teams) {

        HTML_code = '<tr>';
        HTML_code += '<th> POŘADÍ </th>';
        HTML_code += '<th> JMÉNO </th>';
        HTML_code += '<th> ZABITÍ </th>';
        HTML_code += '<th> ÚMRTÍ </th>';
        HTML_code += '<th> SKÓRE </th>';
        HTML_code += '</tr>';

        for (i in Teams) {
            Team = Teams[i]

            HTML_code += '<tr>';

            HTML_code += '<td align="center">';
            HTML_code += Team.position
            HTML_code += '</td>';

            HTML_code += '<td align="center">';
            HTML_code += '<span style="color: ' + Team.color + '; font-weight: 400;">' + Team.name + '</span>' + '<br>';
            HTML_code += '</td>';

            HTML_code += '<td align="center">';
            HTML_code += Team.kills_count
            HTML_code += '</td>';

            HTML_code += '<td align="center">';
            HTML_code += Team.deaths_count
            HTML_code += '</td>';

            HTML_code += '<td align="center">';
            HTML_code += Team.points
            HTML_code += '</td>';

            HTML_code += '</tr>';
        }
        $("#state-teams").html(HTML_code);
        setTimeout(GetActualTeam, 1000);
    });
}

$(document).ready(function () {
    GetActualTeam();
});
