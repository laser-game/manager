// initial variables from DEFAULT
var Team = [];
var Color = [];
var Player = [];
function InitVariables() {
    for (i in DEFAULT.COLOR) {
        Color[i] = Object();
        Color[i].RGB = DEFAULT.COLOR[i];
        Color[i].Members = 0;
        Color[i].Available = false;
    }

    for (i in DEFAULT.DEFAULT_TEAM_NAME) {
        Team[i] = Object();
        Team[i].ID = i;
        Team[i].Name = "";
        Team[i].Color = 0;
        Team[i].Available = false;
    }

    for (i = 0; i < DEFAULT.MAX_PLAYERS; i++) {
        Player[i] = new Object();
        Player[i].ID = i;
        Player[i].Name = "";
        Player[i].Color = 0;
        Player[i].Battery = 100;
        Player[i].Available = false;
    }
}
