$(function () {
  	$("#mail").focus();

	$('.form-anti-bot, .form-anti-bot-2').hide(); // hide inputs from users
	var answer = $('.form-anti-bot input#anti-bot-a').val(); // get answer
	$('.form-anti-bot input#anti-bot-q').val( answer ); // set answer into other input

	if ( $('form#mail input#anti-bot-q').length == 0 ) {
    	var current_date = new Date();
		var current_year = current_date.getFullYear();
		$('form#mail').append('<input type="hidden" name="anti-bot-q" id="anti-bot-q" value="' + current_year + '" />'); // add whole input with answer via javascript to form
    }
});


$('#mail').submit(function (evtObj) {
    evtObj.preventDefault();
    var form = $(this);
    
    $.ajax({
        url: $(form).attr('action'),
        type: 'POST',
        data: form.serialize(),

        success: function (data) {
            if (data === 'Письмо отправлено') {
                $("#info-suc").html('Спасибо! Ваше сообщение было отправленно.');
                document.getElementById("mail").reset();
                document.getElementById("info-suc").style.display ="block";
                document.getElementById("info-err").style.display ="none";
                $('#mail').hide();
		            
            } else {
                $("#info-err").html(data);
            }
        },
        error: function (data) {
            $("#info-err").html('Результат выполнения: ' + data);
        }
    });
});