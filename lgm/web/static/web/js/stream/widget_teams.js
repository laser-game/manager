// načteme informace týmech
function GetActualTeam() {
    $.getJSON("/api/actual-teams", function (Team) {
        var order = [];
        var position;
        for (j = 0; j < Team.length; j++) {
            position = Team.length + 1;
            for (i = 0; i < Team.length; i++) {
                if (Team[i].Position < position && Team[i].enable) {
                    var order_test = true;
                    if (order.length) {
                        for (k = 0; k < order.length; k++) {
                            if (order[k] == Team[i].id) {
                                order_test = false;
                                break;
                            }
                        }
                    }
                    if (order_test) {
                        position = Team[i].Position;
                        order[j] = Team[i].id;
                    }
                }
            }
        }

        HTML_code = '<tr>';
        HTML_code += '<th> POŘADÍ </th>';
        HTML_code += '<th> JMÉNO </th>';
        HTML_code += '<th> ZABITÍ </th>';
        HTML_code += '<th> ÚMRTÍ </th>';
        HTML_code += '<th> SKÓRE </th>';
        HTML_code += '</tr>';

        for (j = 0; j < order.length; j++) {
            i = order[j];
            HTML_code += '<tr>';

            HTML_code += '<td align="center">';
            HTML_code += Team[i].Position.toString();
            HTML_code += '</td>';

            HTML_code += '<td align="center">';
            HTML_code += '<span style="color: ' + Color[Team[i].color_index].rgb + '; font-weight: 400;">' + Team[i].name + '</span>' + '<br>';
            HTML_code += '</td>';

            HTML_code += '<td align="center">';
            HTML_code += Team[i].Kill.toString();
            HTML_code += '</td>';

            HTML_code += '<td align="center">';
            HTML_code += Team[i].Death.toString();
            HTML_code += '</td>';

            HTML_code += '<td align="center">';
            HTML_code += Team[i].Score.toString();
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
