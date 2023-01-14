$('.add_to_basket').click(function () {
    var productId;
    productId = $(this).attr("data-productId");
    $.ajax(
        {
            type: "GET",
            url: "/add-to-cart/" + productId + "/",
            success: function (data) {
                $('.bakset-cnt').text(data)
//                alert('Добавлено')
            }
        })
});

$('.dicrement__item').click(function () {
    var productId;
    productId = $(this).attr("data-productId");
    $.ajax(
        {
            type: "GET",
            url: "/change-quantity/" + productId + "?action=decrease",
            success: function (data) {
                var list = data.split('|')
                let count = list[0]
                let cartLength = list[1]
                $('#cart-product' + productId).text(count)
                $('.bakset-cnt').text(cartLength)
                getSumm();

                console.log(list);
                // alert('Удалено')

            }
        })
});

$('.increment__item').click(function () {
    var productId;
    productId = $(this).attr("data-productId");
    $.ajax(
        {
            type: "GET",
            url: "/change-quantity/" + productId + "?action=increase",
            success: function (data) {
                var list = data.split('|')
                let count = list[0]
                let cartLength = list[1]
                $('#cart-product' + productId).text(count)
                $('.bakset-cnt').text(cartLength)
                getSumm();
                // alert('Добавлено')
            }
        })
});

function getSumm() {
    $.ajax(
        {
            type: "GET",
            url: "/cart-summ/",
            success: function (data) {
                $('#summ').text(data)
            }
        });
}