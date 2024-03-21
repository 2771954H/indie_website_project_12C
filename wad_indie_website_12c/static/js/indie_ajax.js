$(document).ready(function() {
    $('#like_btn').click(function() {
    var gameSlugVar;
    gameSlugVar = $(this).attr('data-gameslug');
    $.get('/indie/like_game/',
    {'game_name_slug': gameSlugVar},
    function(data) {
        $('#like_count').html(data);
        $('#like_btn').hide();
    })
    });
    });