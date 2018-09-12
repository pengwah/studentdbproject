  $(document).ready(function(){
    if($("#edit").val() == "Cancel"){
      $("#save").removeAttr("hidden");
    }
    else{
      $("#save").attr("hidden", "hidden");
    }

    $('#edit').on('click',function(){
      refreshform();
      if($(".form-control").attr("disabled") == "disabled"){
        $(".form-control").removeAttr("disabled");
        $("#edit").val("Cancel");
        $("#save").removeAttr("hidden");
      }
      else{
        $(".form-control").attr("disabled", "disabled");
        $("#edit").val("Edit");
        $("#save").attr("hidden", "hidden");
      }
    });

    $("#submit").submit(function(event){
      var formData = {
        'id'        : $('#id').val(),
        'firstname' : $('#firstname').val(),
        'lastname'  : $('#lastname').val(),
        'birthdate' : $('#birthdate').val(),
        'email'     : $('#email').val(),
        'email2'    : $('#email2').val(),
        'phone1'    : $('#phone1').val(),
        'phone2'    : $('#phone2').val(),
        'street'   : $('#street').val(),
        'city'      : $('#city').val(),
        'zipcode'   : $('#zipcode').val(),
      };

      $.ajaxSetup({
        beforeSend: function(xhr, settings) {
          function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
              var cookies = document.cookie.split(';');
              for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
                }
              }
            }
            return cookieValue;
          }
          if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
          }
        }
      });

      $.ajax({
        type        : 'POST', // define the type of HTTP verb we want to use (POST for our form)
        url         : 'students/create', // the url where we want to POST
        data        : formData, // our data object
        dataType    : 'json', // what type of data do we expect back from the server
        encode       : true,
        success: function (data) {
           if (data) {
             refreshform();
             $(".form-control").attr("disabled", "disabled");
             $("#edit").val("Edit");
             $("#save").attr("hidden", "hidden");
           }},
      });
      event.preventDefault();
    });
  })

  function refreshform(){
    var formData = {
      'id'        : $('#id').val(),
    };
    $.ajaxSetup({
      beforeSend: function(xhr, settings) {
        function getCookie(name) {
          var cookieValue = null;
          if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
              var cookie = jQuery.trim(cookies[i]);
              // Does this cookie string begin with the name we want?
              if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
              }
            }
          }
          return cookieValue;
        }
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
          // Only send the token to relative URLs i.e. locally.
          xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
      }
    });
    $.ajax({
      type        : 'POST', // define the type of HTTP verb we want to use (POST for our form)
      url         : '/students/refresh', // the url where we want to POST
      data        : formData, // our data object
      dataType    : 'json', // what type of data do we expect back from the server
      encode       : true,

      success: function (data) {
         if (data) {
           var jsonparsed = JSON.parse(data[0].student)[0].fields;
           $('#firstname').val(jsonparsed.firstname);
           $('#lastname').val(jsonparsed.lastname);
           $('#birthdate').val(jsonparsed.birthdate);
           $('#email').val(jsonparsed.email);
           $('#email2').val(jsonparsed.email2);
           $('#phone1').val(jsonparsed.phone1);
           $('#phone2').val(jsonparsed.phone2);
           $('#street').val(jsonparsed.street);
           $('#city').val(jsonparsed.city);
           $('#zipcode').val(jsonparsed.zipcode);
         }},
    });
  }
