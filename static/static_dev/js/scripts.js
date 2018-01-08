$(document).ready(function(){
    var form = $('#form_buying_product');
    console.log(form);
    form.on('submit', function(e){
        e.preventDefault();
        console.log('123');
        var nmb = $('#number').val();
        console.log(nmb);
        var submit_btn = $('#submit_btn');
        var product_id =  submit_btn.data("product_id");
        var name = submit_btn.data("name");
        var price = submit_btn.data("price");
        console.log(product_id );
        console.log(name);
    })});

//
//     $('.basket-container').on('click', function(e) {
//         e.preventDefault();
//         $('.basket-item').removeClass('hidden');
//     });
//     $('.basket-container').mouseover(function() {
//
//         $('.basket-item').removeClass('hidden');
//     });
//     $('.basket-container').mouseout(function() {
//
//         $('.basket-item').addClass('hidden');
//     });
// });