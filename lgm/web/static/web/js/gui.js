function CheckBoxHTML(checkbox, checked) {
    if (checked) {
        checkbox.html('<img src="/static/web/img/checked.svg" class="checkbox">');
        checkbox.val(true);
    }
    else {
        checkbox.html('<img src="/static/web/img/unchecked.svg" class="checkbox">');
        checkbox.val(false);
    }
}

function RadioHTML(radio, checked) {
    if (checked) {
        radio.html('<img src="/static/web/img/radio_on.svg" class="radio">');
        radio.val(true);
    }
    else {
        radio.html('<img src="/static/web/img/radio_off.svg" class="radio">');
        radio.val(false);
    }
}

function SetCheckBox(checkbox, checked) {
    var checkbox_id = '#' + 'CheckBox-' + checkbox;
    if (checked || checked == 'checked') {
        CheckBoxHTML($(checkbox_id), true);
    }
    else {
        CheckBoxHTML($(checkbox_id), false);
    }
}

function SetRadio(radio_group, value) {
    var radio_class = '.' + 'Radio-' + radio_group;
    var radio_active_id = '#' + 'Radio-' + radio_group + '-' + value;
    $(radio_class).each(function(){RadioHTML($(this), false);});
    if (value < $(radio_class).length) {
        RadioHTML($(radio_active_id), true);
    }
}

function GetCheckBox(checkbox) {
    var checkbox_id = '#' + 'CheckBox-' + checkbox;
    var value = false;
    if ($(checkbox_id).val() === 'true') {
        value = true;
    }
    return value;
}

function GetRadio(radio_group) {
    var radio_class = '.' + 'Radio-' + radio_group;
    var value = false;
    $(radio_class).each(function() {
        if ($(this).val() === 'true') {
            value = parseInt($(this).attr('id').split('Radio-' + radio_group + '-')[1]);
        }
    });
    return value;
}

$(document).ready(function () {
    $("[class^='Radio']").each(function() {
        RadioHTML($(this), false);
    });

    $("[id^='CheckBox']").each(function() {
        CheckBoxHTML($(this), false);
    });

    $("[class^='Radio']").click(function () {
        $('.' + $(this).attr("class")).each(function(){RadioHTML($(this), false);});
        RadioHTML($(this), true);
    });

    $("[id^='CheckBox']").click(function () {
        var checkbox = $(this).attr('id').split('CheckBox-')[1];
        SetCheckBox(checkbox, !GetCheckBox(checkbox));
    });
});
