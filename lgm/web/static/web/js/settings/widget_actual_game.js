$(document).ready(function () {
    // načteme informace o aktuální hře
    function GetActualGame() {
        $.getJSON("/api/actual-game", function (data) {
            $("#actual-game-type").text(data.GameType);
            $("#actual-players").text(data.Players);
            $("#actual-start-time").text(data.StartTime);
            $("#actual-time-to-end").text(data.EndTime);
        });

        setTimeout(GetActualGame, 1000);
    }
    //setTimeout(GetActualGame, 1000);
});
