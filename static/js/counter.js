$(document).ready(function(){
        $('h1').hover(function(){
            $(this).css('color', 'yellow');
            },function(){
            $(this).css('color', 'orange');
        });
    })