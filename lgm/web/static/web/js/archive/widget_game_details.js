// načteme informace o aktuální hře
function GetHistoryGameDetails(data) {
    $("#actual-game-type").text(data.GameType);
    $("#actual-players").text(data.Players);
    $("#actual-start-time").text(data.GameTime);
    $("#actual-time-to-end").text(data.StartTime);
}
