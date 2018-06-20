// initial variables from DEFAULT
var Team = [];
var Color = [];
var Player = [];
function InitVariables() {
    for (i in DEFAULT.COLOR) {
        Color[i] = Object();
        Color[i].rgb = DEFAULT.COLOR[i];
        Color[i].members = 0;
        Color[i].anable = false;
    }

    for (i in DEFAULT.DEFAULT_TEAM_NAMES) {
        Team[i] = Object();
        Team[i].id = i;
        Team[i].name = "";
        Team[i].color_index = 0;
        Team[i].anable = false;
    }

    for (i = 0; i < DEFAULT.MAX_PLAYERS; i++) {
        Player[i] = new Object();
        Player[i].address = i;
        Player[i].name = "";
        Player[i].color_index = -1;
        Player[i].battery = 100;
        Player[i].anable = false;
    }
}
