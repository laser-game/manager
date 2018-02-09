window.Check = {
    init() {
        $("[id^='Check']").each(function () {
            Check._html($(this), false);
        }).click(function () {
            var checkbox = $(this).attr('id').split('Check-')[1];
            Check.set(checkbox, !Check.get(checkbox));
        });
    },
    _html(checkbox, checked) {
        if (checked) {
            checkbox.html('<img src="/static/web/img/checked.svg" class="checkbox">');
            checkbox.val(true);
        }
        else {
            checkbox.html('<img src="/static/web/img/unchecked.svg" class="checkbox">');
            checkbox.val(false);
        }
    },

    set(checkbox, checked) {
        var checkbox_id = '#' + 'Check-' + checkbox;
        if (checked || checked == 'checked') {
            Check._html($(checkbox_id), true);
        }
        else {
            Check._html($(checkbox_id), false);
        }
    },

    get(checkbox) {
        var checkbox_id = '#' + 'Check-' + checkbox;
        var value = false;
        if ($(checkbox_id).val() === 'true') {
            value = true;
        }
        return value;
    }
};

window.Radio = {
    init() {
        $("[class^='Radio']").each(function () {
            Radio._html($(this), false);
        }).click(function () {
            $('.' + $(this).attr("class")).each(function () {
                Radio._html($(this), false);
            });
            Radio._html($(this), true);
        });
    },
    _html(radio, checked) {
        if (checked) {
            radio.html('<img src="/static/web/img/radio_on.svg" class="radio">');
            radio.val(true);
        }
        else {
            radio.html('<img src="/static/web/img/radio_off.svg" class="radio">');
            radio.val(false);
        }
    },

    set(radio_group, value) {
        var radio_class = '.' + 'Radio-' + radio_group;
        var radio_active_id = '#' + 'Radio-' + radio_group + '-' + value;
        $(radio_class).each(function () {
            Radio._html($(this), false);
        });
        if (value < $(radio_class).length) {
            Radio._html($(radio_active_id), true);
        }
    },

    get(radio_group) {
        var radio_class = '.' + 'Radio-' + radio_group;
        var value = false;
        $(radio_class).each(function () {
            if ($(this).val() === 'true') {
                value = parseInt($(this).attr('id').split('Radio-' + radio_group + '-')[1]);
            }
        });
        return value;
    }
};

$(document).ready(function () {
    Check.init();
    Radio.init();
});
