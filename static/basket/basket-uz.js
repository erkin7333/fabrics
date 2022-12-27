$(document).ready(function(){
    loadallprice();
	quantity_goods();
	producttobacket();
	loadbasket();
    
    $('.add_to_basket').click(function(){
		var productId = $(this).attr("product");
		$.post('/basket/basket-uz.php', { id: productId, action: 'addtobasket' }, function(result) {
            quantity_goods();
            $('#'+productId).html('<span class="circle"><i class="fa fa-check"></i></span>'); 
            $('#'+productId).removeClass('add_to_basket').removeAttr('product'); 
        });
	});
	
	$('.add_basket').click(function(){
		var productId = $(this).attr("product");
		var count =  $('.cnt-input').attr('data-quantity');
		$.post('/basket/basket-uz.php', { id: productId, count: count, action: 'addtobasket' }, function(result) {
            quantity_goods();
            $('#'+productId).text('Товар в корзине');
            $('#'+productId).removeClass('add_basket').removeAttr('product'); 
        });
	});
	
	
	$(document).on('click', '.product-remove', function(){
		var iid = $(this).attr("iid");
		$.post('/basket/basket-uz.php', { id: iid, action: 'remove' }, function(rem) {
          if(rem == 1){
            $('.block-'+ iid).fadeOut();
            quantity_goods();
            loadallprice();
    		  }
        });
	});

	$(document).on('click', '.count-minus', function(){
		var iid = $(this).attr("iid");
		$.post('/basket/basket-uz.php', { bid: iid, action: 'minus' }, function(min) {
            $("#input-id" + iid).val(min);
            if(min == '0'){ $('.block-'+ iid).fadeOut(); }
            quantity_goods();
            // переменная с ценой товара
            var priceProduct = $("#tovar" + iid).attr("price");
          //цену умножаем на кол-во
          resulTotal = Number(priceProduct) * Number(min);
          $("#tovar" + iid).text(intSpace(resulTotal));	
          loadallprice();
        });

	});
	
	$(document).on('click', '.count-plus', function(){
		var iid = $(this).attr("iid");
		$.post('/basket/basket-uz.php', { bid: iid, action: 'plus' }, function(max) {
        $("#input-id" + iid).val(max);
			quantity_goods();
			// переменная с ценой товара
			var priceProduct = $("#tovar" + iid).attr("price");
			//цену умножаем на кол-во
			resulTotal = Number(priceProduct) * Number(max);
			//console.log(priceProduct);
			$("#tovar" + iid).text(intSpace(resulTotal));	
			loadallprice();
        });		
	});
	
	
	$(document).on('keypress', '.count-input', function(e){
		
		if (e.keyCode == 13){
			var iid = $(this).attr("iid");
			var incount = $("#input-id"+iid).val();
			//console.log(incount);
            $.post('/basket/basket-uz.php', { bid: iid , count: incount, action: 'countinput' }, function(cinp) {
                $("#input-id" + iid).val(cinp);
				quantity_goods();
				// переменная с ценой товара
				var priceProduct = $("#tovar" + iid).attr("price");
				//цену умножаем на кол-во
				resulTotal = Number(priceProduct) * Number(cinp);
				$("#tovar" + iid).text(intSpace(resulTotal));
				loadallprice();
            });
		}
	});
	
	// Очистить корзину
    $(document).on('click', '.clear-cart', function(){
        $.post('/basket/basket-uz.php', { clear: 'clear' }, function(data){
            if(data == 1){
                quantity_goods();
                $('.basket-delete-info').show();
                $('.basket-items').hide();
                $('.recalculate-form').hide();
                $('.orders-details').hide();
            } return false;
        });    
	});	


    /**
    *  Результат покупок кол-во выбранного товара
    **/
	function quantity_goods(){
      	$.post('/basket/basket-uz.php', {action: 'quantity'}, function(quantity) {
    		  $('.bakset-cnt').text(quantity);	
        });
	}
	
/*
	amountDue();
	
	$('input[name=delivery]').change(function() {
        var delivery = $(this).val();
        var deliveryPrice = $(this).attr('data-delivery');
        
        console.log(deliveryPrice);
        $.post('/basket/basket-uz.php', { action: 'typedelivery', delivery: delivery, price: deliveryPrice }, function(data){
            $('.delivery').text(data.itog);
            amountDue();
        }, 'json');
    });
    
	function amountDue(){
    	$.post('/basket/basket-uz.php', {action: 'amountdue'}, function(data) {
            $('.amount-due').text(data.amountdue);
            if(data.serviceprice != null){$('.delivery').text(data.serviceprice);}
            $('.priceUpdate').val(data.priceupdate);
            if(data.servicename != null)
                $('#'+data.servicename).attr('checked', true);
             else
                 $('#'+data.servicename).attr('checked', false);
            if (data.sum != '' && data.sum < 100000){
                $('#free').attr('disabled', true); 
            }
        }, 'json');
	}
	
*/
	
	/**
  *  Вывод общей суммы в корзине
  **/
	function loadallprice(){
    	$.post('/basket/basket-uz.php', {action: 'loadallprice'}, function(data) {
        	
            if(data.status == 1){	
                $('.totalprice-products').text(data.allprice);
                $('.totalprice').text(data.allprice);
                
            } else {	
    				//$('.totalprice-products').text(data);
            }
    			//recountProduct( $(thisClick).closest(".product-tablerow") ); //пересчёт
        }, 'json');
	}
	/**
    *  Товар добавленый в корзину
    *  Получаем массив id товаров 
    *  Для замены текста на кнопке 
    **/
    function producttobacket(){
      	$.post('/basket/basket-uz.php', {action: 'producttobacket'}, function(data) {

        	var dt =	data.split(',');
            if(dt != ''){	
                for (i=0; i < dt.length; i++){
                    $('#'+dt[i]).html('<span class="circle"><i class="fa fa-check"></i></span>'); 
                    $('#'+dt[i]).removeClass('add_to_basket').removeAttr('product'); 
                }	
            } 
        });
	}
	
	/**
  *  Вывод товаров в корзине
  **/
	function loadbasket(){
        $.post('/basket/basket-uz.php', {action: 'loadbasket'}, function(data) {
        	//console.log(data);
            if(data == 0){	
                $('.basket-empty').show();	
                $('.recalculate-form').hide();
                $('.orders-details').hide();
                
            } else {	
                $('.basket-items').html(data);
            }
        });
	}
	
	// Изменение текста при выборе метода оплаты
    $(".payment").change(function () {
        var val = $('.payment:checked').val();
        if(val === 'payme'){
          $('#order').text('Перейти к оплате');
        } else if (val === 'click') {
          $('#order').text('Перейти к оплате');
        }else {
          $('#order').text('Оформить заказ');
        }
    });
  
  
});


$(function() {
    $.mask.definitions['~'] = "[+-]";
    $(".phone").mask('+998 11111-11-11');
  
});



