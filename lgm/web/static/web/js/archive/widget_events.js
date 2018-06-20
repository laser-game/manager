// načteme poslední události
function SetHistoryEvents(Events) {
    var HTML_code;

    HTML_code = '<tr>';
    HTML_code += '<th> ČAS </th>';
    HTML_code += '<th> JMÉNO </th>';
    HTML_code += '<th> CO </th>';
    HTML_code += '<th> JMÉNO </th>';
    HTML_code += '</tr>';

    for (i = 0; i < Events.length; i++) {
        HTML_code += '<tr>';

        HTML_code += '<td align="center">';
        HTML_code += Events[i].Time.toString();
        HTML_code += '</td>';

        HTML_code += '<td align="center">';
        HTML_code += '<span style="color: ' + Color[Events[i].Color1].rgb + '; font-weight: 400;">' + Events[i].Name1 + '</span>' + '<br>';
        HTML_code += '</td>';

        HTML_code += '<td align="center">';
        HTML_code += Events[i].Event.toString();
        HTML_code += '</td>';

        HTML_code += '<td align="center">';
        HTML_code += '<span style="color: ' + Color[Events[i].Color2].rgb + '; font-weight: 400;">' + Events[i].Name2 + '</span>' + '<br>';
        HTML_code += '</td>';

        HTML_code += '</tr>';
    }
    $("#archive-events").html(HTML_code);
}
