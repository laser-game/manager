// nastaví checkox
function SetCheckBox(id, checked) {
    if (checked) {
        $(id).html('<img src="/static/web/img/checked.svg" class="checkbox">');
    }
    else {
        $(id).html('<img src="/static/web/img/unchecked.svg" class="checkbox">');
    }
}

// nastaví radio
function SetRadio(class_name, value) {
    var len = $("." + class_name).length;
    for (i = 0; i < len; i++) {
        var id = "#" + class_name + "-" + i.toString();
        if (SetGame.Fn == i) {
            $(id).html('<img src="/static/web/img/radio_on.svg" class="radio">');
        }
        else {
            $(id).html('<img src="/static/web/img/radio_off.svg" class="radio">');
        }
    }
}
