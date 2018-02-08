// načteme informace odehraných hrách
function GetHistoryGames() {
    $.getJSON("/api/archive-games", function (Game) {
        HTML_code = '<tr>';
        HTML_code += '<th> DATUM </th>';
        HTML_code += '<th> TYP HRY </th>';
        HTML_code += '<th> POČET HRÁČŮ </th>';
        HTML_code += '</tr>';

        for (i = 0; i < Game.length; i++) {
            HTML_code += '<tr class="archive-game" id="archive-game-' + i.toString() + '">';

            HTML_code += '<td align="center">';
            HTML_code += Game[i].Date.toString();
            HTML_code += '</td>';

            HTML_code += '<td align="center">';
            HTML_code += '<span style="color: cyan; font-weight: 400;">' + Game[i].Name + '</span>';
            HTML_code += '</td>';

            HTML_code += '<td align="center">';
            HTML_code += Game[i].Players.toString();
            HTML_code += '</td>';

            HTML_code += '</tr>';
        }
        $("#history-games").html(HTML_code);
        // clicknutí na tlačítko vyčistit
        $(".archive-game").click(function () {
            var id = parseInt($(this).attr("id").split("-")[2]);
            // načtene informace o hráčích
            $.getJSON("/api/archive-players/" + id.toString(), function (Players) {
                SetHistoryPlayers(Players);
            });
            $.getJSON("/api/archive-events/" + id.toString(), function (Events) {
                SetHistoryEvents(Events);
            });
            $.getJSON("/api/archive-game-details/" + id.toString(), function (data) {
                GetHistoryGameDetails(data)
            });
        });
        setTimeout(GetHistoryGames, 1000);
    });
}

$(document).ready(function () {
    GetHistoryGames();
});
