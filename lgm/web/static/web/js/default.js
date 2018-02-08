// get default variables
var DEFAULT;
function GetDefault() {
    $.getJSON("/api/default", function (json) {
        DEFAULT = JSON.parse(JSON.stringify(json));
        InitVariables();
    });
}
