function SetCheckBox(id, checked) {
    if (checked) {
        $(id).html('<img src="/static/web/img/checked.svg" class="checkbox">');
    }
    else {
        $(id).html('<img src="/static/web/img/unchecked.svg" class="checkbox">');
    }
}

function RadioHTML(radio, checked) {
    if (checked || checked == 'checked') {
        radio.html('<img src="/static/web/img/radio_on.svg" class="radio">');
        radio.val(true);
    }
    else {
        radio.html('<img src="/static/web/img/radio_off.svg" class="radio">');
        radio.val(false);
    }
}

function SetRadio(radio_group, value) {
    var radio_class = '.' + 'Radio-' + radio_group;
    var radio_active_id = '#' + 'Radio-' + radio_group + '-' + value;
    if (value < $(radio_class).length)
    {
        $(radio_class).each(function(){RadioHTML($(this), false);});
        RadioHTML($(radio_active_id), true);
    }
}

function GetRadio(radio_group) {
    var radio_class = '.' + 'Radio-' + radio_group;
    var value = false;

    $(radio_class).each(function() {
        if ($(this).val() === 'true') {
            value = $(this).attr('id').split('-');
            value = parseInt(value[value.length - 1]);
        }
    });

    return value;
}

$(document).ready(function () {
    $("[class^='Radio']").each(function() {
        RadioHTML($(this), false);

    });

    $("[class^='Radio']").click(function () {
        $('.' + $(this).attr("class")).each(function(){RadioHTML($(this), false);});
        RadioHTML($(this), true);
    });
});
