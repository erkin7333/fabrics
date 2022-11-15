$(document).ready(function(){
	
	amountDue();
	
	$('input[name=delivery]').change(function() {
        var delivery = $(this).val();
        var deliveryPrice = $(this).attr('data-delivery');
        
        $.post('/basket/basket-uz.php', { action: 'typedelivery', delivery: delivery, price: deliveryPrice }, function(data){
                $('.delivery').text(data.itog);
            amountDue();
        }, 'json');
    });
    
	function amountDue(){
    	$.post('/basket/basket-uz.php', {action: 'amountdue'}, function(data) {
            $('.amount-due').text(data.amountdue);
            if(data.serviceprice != ''){
                $('.delivery').text(data.serviceprice);
            } else {
                 $('.delivery').text(0);
            }
            if(data.servicename != ''){
                $('#'+data.servicename).attr('checked', true);
            }
            if (data.sum != '' && data.sum < 100000){
                $('#free').attr('disabled', true); 
                $('#free').attr('checked', false);
                $('#free').hide();
                $('.free_box').hide();
            }
        }, 'json');
	}
});


//$.validator.messages.required = '';
$("#mailorder").validate({
    errorElement: "span",
    errorClass: "error",
    onfocusout: function(element) {$(element).valid()},
    rules: {
      name: {required: true,maxlength: 58},
      phone: {maxlength: 18,required: true},
     // email: {email: true,maxlength: 50,required: true},
      address: {required: true},
      payment: {required: true},
      delivery: {required: true}
      
    },
    messages: {
        name: {required: "Ismingizni ko\'rsating."}, 
        phone: {required: "Telefon raqamingizni ko\'rsating."},
       // email: {required: "Вы не указали email"},
        address: {required: "Yetkazib berish manzilini ko\'rsating."},
        payment: { required: "To\'lov usulini tanlang"},
        delivery: { required: "Yetkazib berish shartlarini tanlang"}
    },
    //ignore: ":hidden:not(:checkbox)",
    errorPlacement: function (error, element) {  
        if(element.attr("name") == "payment"){
            error.appendTo("#error_payment");
            return;
        } else if(element.attr("name") == "delivery"){
            error.appendTo("#error_delivery");
            return;
        } else { 
         return false;
        }
    },
    submitHandler: function(b) {  
        $("#order").attr("disabled", "disabled").text("  Подождите ...  "); // .attr("disabled", "disabled")
        $.post($("#mailorder").attr("action"), $("#mailorder").serialize()).done(function (c) {
            console.log(c)
            var d = JSON.parse(c);
            $('.form-payments').html(d.form);
            $("#order_success").html('<h3 class="info-suc h-clear text-center" >Спасибо <b>'+d.name+'</b> за покупку! <br>Ваш заказ под номером <b>№'+d.numorder+'</b> принят. <br>Наш менеджер свяжемся с Вами в ближайшее время для уточнения заказа!</h3>');
            $("#order").unbind().val("отправлено");

            $('#mailorder').hide();
            $('#delivery_method').hide();
            
        }).fail(function (b) {  
            if (b.status == 400) { 
                $('#mail_order').show();
                $('#delivery_method').show();
                $("#order").text("Отправить");
            }
        })
    },
});
