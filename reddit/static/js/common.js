function notify_this(message_text, message_type) {
    $.notify({
        message: message_text
    }, {
        // settings
        type: message_type,
        placement: {
            from: "bottom",
            align: "right"
        },
        animate: {
            enter: 'animated fadeInDown',
            exit: 'animated fadeOutUp'
        }
    });
}
$.fn.extend({
    animateCss: function (animationName) {
        var animationEnd = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';
        this.addClass('animated ' + animationName).one(animationEnd, function () {
            $(this).removeClass('animated ' + animationName);
            $(this).hide()
        });
        return this;
    },
    showProgress: function (animationName, display, selector) {
        if (display == 'show') {
            this.css({'display': 'block'})
        } else {
            setTimeout(function () {
                $('#progress-dialog').css({'display': 'none'})
            }, 500)
        }
        var animationEnd = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';
        this.addClass('animated ' + animationName).one(animationEnd, function () {
            $(this).removeClass('animated ' + animationName);
        });
        return this;
    }
});
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        //$('.overlay').fadeIn()
        if (settings.type == 'POST' || settings.type == 'PUT' || settings.type == 'DELETE') {

            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    },
    complete: function (xhr) {
    }
});
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
function show_progress_bar(message, progress_type) {
    if (progress_type == 'long') {
        $('#progress-dialog').showProgress('bounceIn', 'show')
        $('#progress-dialog>.progress-dialog-text').text(message)
        $('.overlay').fadeIn()
    } else {
        $('.overlay-with-loader').fadeIn()
    }
}
function hide_progress_bar() {
    $('#progress-dialog').showProgress('bounceOut', 'hide')
    $('#progress-dialog>.progress-dialog-text').text('')
    $('.overlay').fadeOut()
    $('.overlay-with-loader').fadeOut()
}