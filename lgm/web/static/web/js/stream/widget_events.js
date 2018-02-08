// načteme poslední události
function GetActualEvents() {
    $.getJSON("/api/actual-events", function (Events) {
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
            HTML_code += '<span style="color: ' + Color[Events[i].Color1].RGB + '; font-weight: 400;">' + Events[i].Name1 + '</span>' + '<br>';
            HTML_code += '</td>';

            HTML_code += '<td align="center">';
            HTML_code += Events[i].Event.toString();
            HTML_code += '</td>';

            HTML_code += '<td align="center">';
            HTML_code += '<span style="color: ' + Color[Events[i].Color2].RGB + '; font-weight: 400;">' + Events[i].Name2 + '</span>' + '<br>';
            HTML_code += '</td>';

            HTML_code += '</tr>';
        }
        $("#events").html(HTML_code);


        setTimeout(GetActualEvents, 1000);
    });
}

$(document).ready(function () {
    GetActualEvents();
});
