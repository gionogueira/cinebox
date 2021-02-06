$(document).ready(function(){
    $("#id_titulo").focusout(function(){
        var titulo = $("#id_titulo").val();

        var urlstr = "http://www.omdbapi.com/?apikey=1e2d38e1&t="+ titulo;

        $.ajax({
            url : urlstr,
            type : "get",
            dataType : "json",
            success : function(data) {
                console.log(data);

                $("#id_ano").val(data.Year);
                $("#id_sinopse").val(data.Plot);
                $("#id_produtora").val(data.Production);
            },
            error : function(erro) {
                console.log(erro);
            }
        });
    });
});

$(document).ready(function(){
    $("#id_titulo").keyup(function(){
        var titulos = $("#id_titulo").val();
        var urlstr = "http://www.omdbapi.com/?apikey=1e2d38e1&s="+ titulos;

        if(titulos.length > 2){
            $.ajax({
                url : urlstr,
                method : "POST",
                dataType : "json",
                success : function(data) {
                    for(let prop of data.Search) {
                        $("#response").append('<li>'+ prop.Title +'</li>'); 
                        console.log(prop);
                        
                    }
                }
            });
        }
    });
    
    $(document).on('click', 'li', function(){
        var title = $(this).text();
        $("#id_titulo").val(title);
        $("#response").html("");
    });    
});

$('.carousel2').slick({
    dots: true,
    infinite: true,
    slidesToShow: 4,
    slidesToScroll: 4
});





