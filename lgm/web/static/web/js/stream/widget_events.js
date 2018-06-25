// načteme poslední události
function GetActualEvents() {
    $.getJSON("/api/actual-events", function (Events) {
        HTML_code = '<tr>';
        HTML_code += '<th> ČAS </th>';
        HTML_code += '<th> JMÉNO </th>';
        HTML_code += '<th> UDÁLOST </th>';
        HTML_code += '<th> JMÉNO </th>';
        HTML_code += '</tr>';

        for (i in Events) {
            Event = Events[i]

            HTML_code += '<tr>';

            HTML_code += '<td align="center">';
            HTML_code += Event.time;
            HTML_code += '</td>';

            HTML_code += '<td align="center">';
            HTML_code += '<span style="color: ' + Event.color1 + '; font-weight: 400;">' + Event.name1 + '</span>' + '<br>';
            HTML_code += '</td>';

            HTML_code += '<td align="center">';
            switch (Event.identifier) {
                case 'K':
                    HTML_code += 'kill';
                    break;
                case 'F':
                    HTML_code += 'friendly fire';
                    break;
                case 'T':
                    HTML_code += 'tap';
                    break;
                case 'B':
                    HTML_code += 'bonus';
                    break;
                default:
                    break;
            }
            HTML_code += '</td>';

            HTML_code += '<td align="center">';
            HTML_code += '<span style="color: ' + Event.color2 + '; font-weight: 400;">' + Event.name2 + '</span>' + '<br>';
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
