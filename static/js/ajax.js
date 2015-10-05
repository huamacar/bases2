/**
 * Created by alejandro on 18/09/15.
 */
$(function(){
    $('#busquedaCaja').keyup(function(){
        $.ajax({
            type: "POST",
            url: "/Caja/busqueda/",
            data:{
                'search_text'   :   $('#busquedaCaja').val(),
                'csrfmiddlewaretoken'   :   $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess,
            dataType:'html'

        });

    });

    $('#busquedaAutorizacion').keyup(function(){
    $.ajax({
        type: "POST",
        url: "/Autorizacion/busqueda/",
        data:{
            'search_text'   :   $('#busquedaAutorizacion').val(),
            'csrfmiddlewaretoken'   :   $("input[name=csrfmiddlewaretoken]").val()
        },
        success: searchSuccess,
        dataType:'html'

    });

    });

    $('#busquedaTarjeta').keyup(function(){
    $.ajax({
        type: "POST",
        url: "/ListaNegra/busqueda/",
        data:{
            'search_text'   :   $('#busquedaTarjeta').val(),
            'csrfmiddlewaretoken'   :   $("input[name=csrfmiddlewaretoken]").val()
        },
        success: searchSuccess,
        dataType:'html'

    });

    });

     $('#busquedaAfiliado').keyup(function(){
    $.ajax({
        type: "POST",
        url: "/Afiliado/busqueda/",
        data:{
            'search_text'   :   $('#busquedaAfiliado').val(),
            'csrfmiddlewaretoken'   :   $("input[name=csrfmiddlewaretoken]").val()
        },
        success: searchSuccess,
        dataType:'html'

    });

    });

     $('#busquedaCliente').keyup(function(){
    $.ajax({
        type: "POST",
        url: "/Clientes/busqueda/",
        data:{
            'search_text'   :   $('#busquedaCliente').val(),
            'csrfmiddlewaretoken'   :   $("input[name=csrfmiddlewaretoken]").val()
        },
        success: searchSuccess,
        dataType:'html'

    });

    });
     $('#busquedaEmisor').keyup(function(){
    $.ajax({
        type: "POST",
        url: "/Emisor/busqueda/",
        data:{
            'search_text'   :   $('#busquedaEmisor').val(),
            'csrfmiddlewaretoken'   :   $("input[name=csrfmiddlewaretoken]").val()
        },
        success: searchSuccess,
        dataType:'html'

    });

    });
});

function searchSuccess(data, textStatus, jqXHR)
{
    $('#search-results').html(data)
}

 $(function() {
    $( "#datepicker" ).datepicker();
  });