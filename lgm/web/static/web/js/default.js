// get default variables
var DEFAULT;
function GetDefault() {
    $.getJSON("/default", function (json) {
        DEFAULT = JSON.parse(JSON.stringify(json));
        InitVariables();
    });
}
