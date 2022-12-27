$(function () {
  	$("#wholesalers").focus();

	$('.form-anti-bot, .form-anti-bot-2').hide(); // hide inputs from users
	var answer = $('.form-anti-bot input#anti-bot-a').val(); // get answer
	$('.form-anti-bot input#anti-bot-q').val( answer ); // set answer into other input

	if ( $('form#wholesalers input#anti-bot-q').length == 0 ) {
    	var current_date = new Date();
		var current_year = current_date.getFullYear();
		$('form#wholesalers').append('<input type="hidden" name="anti-bot-q" id="anti-bot-q" value="' + current_year + '" />'); // add whole input with answer via javascript to form
    }
});


$('#wholesalers').submit(function (evtObj) {
    evtObj.preventDefault();
    var form = $(this);
    
    $.ajax({
        url: $(form).attr('action'),
        type: 'POST',
        data: form.serialize(),

        success: function (data) {
            if (data === 'Письмо отправлено') {
                $("#infosuc").html('Спасибо! Ваше сообщение было отправленно.');
                document.getElementById("wholesalers").reset();
                document.getElementById("infosuc").style.display ="block";
                document.getElementById("infoerr").style.display ="none";
                $('#wholesalers').hide();
		            
            } else {
                $("#infoerr").html(data);
            }
        },
        error: function (data) {
            $("#infoerr").html('Результат выполнения: ' + data);
        }
    });
});