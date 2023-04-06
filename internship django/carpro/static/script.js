$.get('getbrands', function(data, status){
    brands = JSON.parse(data)["brands"];
    // console.log(JSON.parse(data)["brands"]);
    for(var i in brands){
            var opt = new Option(brands[i]);
            $('#selection').append(opt);
            //console.log(models[i]);
        }
})

// function changed(params) {
//     $.post('getmodels',
//     {
//         brand:params,
//         csrfmiddlewaretoken: "{{csrf_token}}",
//     },
//     function(data, status){
//         //console.log(data+"pavannnnn"+status);
//         models = JSON.parse(data)["models"];
//         $('#model_selection').empty();
//         for(var i in models){
//             var opt = new Option(models[i]);
//             $('#model_selection').append(opt);
//             //console.log(models[i]);
//         }
//     })
//     //console.log(params);
// }
function changed(params){
    $.ajax({
        url:"getmodels",
        type:"get",
        data:{
            brand:params,
        },
        success: function(data){
            models = JSON.parse(data)["models"];
            $('#model_selection').empty();
            for(var i in models){
                var opt = new Option(models[i]);
                $('#model_selection').append(opt);
                //console.log(models[i]);
            }
        },
        error:function(xhr){
            console.log("error");
        }
    });
}

for(var i=1; i<=25; i++){
    var o = new Option(i);
    $('#age').append(o);
}