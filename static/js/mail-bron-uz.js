$(function () {
  	$("#mail-bron").focus();

	$('.form-anti-bot, .form-anti-bot-2').hide(); // hide inputs from users
	var answer = $('.form-anti-bot input#anti-bot-a').val(); // get answer
	$('.form-anti-bot input#anti-bot-q').val( answer ); // set answer into other input

	if ( $('form#mail-bron input#anti-bot-q').length == 0 ) {
    	var current_date = new Date();
		var current_year = current_date.getFullYear();
		$('form#mail-bron').append('<input type="hidden" name="anti-bot-q" id="anti-bot-q" value="' + current_year + '" />'); // add whole input with answer via javascript to form
    }
});

$('#mail-bron').submit(function (e) {
    e.preventDefault();
    var form = $(this);
    
     $.ajax({
            url: $(form).attr('action'),
            type: 'POST',
            data: form.serialize(),
            success: function (data) {
                //console.log(data);
            if (data == 1) {
                $("#messages").html('Спасибо! Ваша заявка принята!');
                document.getElementById("mail-bron").reset();
                document.getElementById("messages").style.display ="block";
                document.getElementById("result").style.display ="none";
                $('#mail-bron').hide();
		            
            } else {
                $("#result").html(data);
            }
        },
        error: function (data) {
            $("#result").html('Результат выполнения: ' + data);
        }
    });
});

	
	
	
	
	
	
	