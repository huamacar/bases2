/**
 * Created by alejandro on 18/09/15.
 */
$(function(){
    $('#search').keyup(function(){
        $.ajax({
            type: "POST",
            url: "/Caja/busqueda/",
            data:{
                'search_text'   :   $('#search').val(),
                'csrfmiddlewaretoken'   :   $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess,
            dataType:'html'

        });

    });

    $('#search2').keyup(function(){
    $.ajax({
        type: "POST",
        url: "/Autorizacion/busqueda/",
        data:{
            'search_text'   :   $('#search2').val(),
            'csrfmiddlewaretoken'   :   $("input[name=csrfmiddlewaretoken]").val()
        },
        success: searchSuccess,
        dataType:'html'

    });

    });

     $('#search3').keyup(function(){
    $.ajax({
        type: "POST",
        url: "/Afiliado/busqueda/",
        data:{
            'search_text'   :   $('#search3').val(),
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