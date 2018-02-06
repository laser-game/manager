function MenuActiveUnderline(MenuUnderline) {
    $(MenuUnderline).addClass("Active");
};

$(document).ready(function () {
    $(".Menu").click(function () {
        $(".MainMenu").children("li").toggleClass("ShowMenu");
        $(".SubMenu").toggleClass("ShowMenu");
    });
});

$(window).resize(function () {
    if ($(".packaging").innerWidth() >= 970) {
        $(".MainMenu").children("li").removeClass("ShowMenu");
        $(".SubMenu").removeClass("ShowMenu");
    }
});