$(document).ready(function () {
    // načteme informace o aktuální hře
    function GetActualGame() {
        $.getJSON("/api/actual-game", function (data) {
            $("#actual-game-type").text(data.name);
            $("#actual-players").text(data.player_count);
            $("#actual-start-time").text(data.started_time);
            $("#actual-time-to-end").text(data.elapsed_time);
            console.log(data);
        });

        setTimeout(GetActualGame, 1000);
    }
    setTimeout(GetActualGame, 1000);
});
