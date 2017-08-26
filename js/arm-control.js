$( document ).ready(function() {

    $("div.servo-control a").on("click",function(event){
      currentUrl = window.location.href+"servo";

      currentData = {
        servo: $(this).data("servo-id"),
        angulo: $(this).data("angulo")
      };
      console.log($(this).attr("servo-id"));
      console.log("current url: "+currentUrl);
      $.ajax(
        {
          url: currentUrl,
          data: JSON.stringify(currentData),
          contentType: "application/json",
          success: function(result){
            console.log("SUCCESS");
            console.log(result);
          },
          type:"POST",
          async:false
        }
      );
    });

});
