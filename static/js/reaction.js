// Function to get csrf token
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Onclick function that takes the clicked emoji and display it below the rant
$(document).on("click",".emoji", function(){
    var rant_id = $('.panel-body').attr('id')
    console.log(rant_id)
    
    csrftoken = getCookie('csrftoken')
    // console.log(csrftoken);

    var attribute = $(this).attr("src");
    // console.log(attribute);

    $("#reactions").append("<img src="+attribute+">");

    var image_title = $(this).attr("title");
    // console.log(image_title);
    // console.log($(this).serialize());


    var url = "/ajax/reaction/"+image_title+"/"+rant_id+"/"
    console.log(url);
    // console.log(attribute.serialize())

    $.ajax({
        'url':url,
        'type':'POST',
        'data': {
            "title":image_title,
            "rant_id":rant_id
        },
        'dataType': 'json',
        beforeSend: function(xhr){
            xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'))
        },
        success:function(data){
            console.log(data['success'])
        }
    }) 

})

// function myFunction() {
//     var x = document.getElementsByClassName("emoji");
//     alt_array = []
//     for(var i = 0; i < x.length; i++){
//         alt_array.push(x[i].title)
//     }
//     document.getElementById("reactions").innerHTML = alt_array
// }

// $("body").bind("ajaxSend", function(elm, xhr, s){
//    if (s.type == "POST") {
//     xhr.setRequestHeader('X-CSRF-Token', getCSRFTokenValue());
//    }
// });


