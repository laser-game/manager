// načteme informace hráčích
function SetHistoryPlayers(Players) {
    var order = [];
    var position;
    for (j = 0; j < Players.length; j++) {
        position = Players.length + 1;
        for (i = 0; i < Players.length; i++) {
            if (Players[i].Position < position && Players[i].anable) {
                var order_test = true;
                if (order.length) {
                    for (k = 0; k < order.length; k++) {
                        if (order[k] == Players[i].ID) {
                            order_test = false;
                            break;
                        }
                    }
                }
                if (order_test) {
                    position = Players[i].Position;
                    order[j] = Players[i].ID;
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
        HTML_code += Players[i].Position.toString();
        HTML_code += '</td>';

        HTML_code += '<td align="center">';
        HTML_code += '<span style="color: ' + Color[Players[i].Color].rgb + '; font-weight: 400;">' + Players[i].Name + '</span>' + '<br>';
        HTML_code += '</td>';

        HTML_code += '<td align="center">';
        HTML_code += Players[i].Kill.toString();
        HTML_code += '</td>';

        HTML_code += '<td align="center">';
        HTML_code += Players[i].Death.toString();
        HTML_code += '</td>';

        HTML_code += '<td align="center">';
        HTML_code += Players[i].Score.toString();
        HTML_code += '</td>';

        HTML_code += '</tr>';
    }
    $("#history-players").html(HTML_code);
}
