

$(document).ready(function () {

    $(".act").click(function () {
        $(this).addClass("active").siblings().removeClass("active");
    });
});
