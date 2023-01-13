$(document).ready(function () {
    
    $('.increment-btn').click(function (e) {
        e.preventDefault();

        var inc_value = $(this).closest('.product_data').find('.quantity-int').val();
        var value = parseInt(inc_value, 10);
        value = isNaN(value) ? 0 : value ;
        if(value < 10 )
        {
            value++;
            $(this).closest('.product_data').find('.quantity-int').val(value);
        }
    });

    $('.decrement-btn').click(function (e) {
        e.preventDefault();

        var inc_value = $(this).closest('.product_data').find('.quantity-int').val();
        var value = parseInt(inc_value, 10);
        value = isNaN(value) ? 0 : value ;
        if(value > 1 )
        {
            value--;
            $(this).closest('.product_data').find('.quantity-int').val(value);
        }
    });

    $('.addToCartBtn').click(function (e) {
        e.preventDefault();

        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var product_qty = $(this).closest('.product_data').find('.quantity-int').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: 'POST',
            url: "http://127.0.0.1:8000/order/",
            data: {
                "product_id": product_id,
                "quantity": product_qty,
                csrfmiddlewaretoken:token
            },
            dataType: 'Dtype',
            success: function(response){
                alertify.success(response.status)
            }

        })
    });
});