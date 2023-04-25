$("#create").click(function(){
    var $loading = $(".loading");
    let mag_check = document.getElementById('mag_check');
    let mag;
    
    if ( mag_check.checked) {mag = 'true';}
    else {mag = 'false';}
    //console.log('http://xs239613.xsrv.jp/api/mapper?lat0=' + lat0 + '&lon0=' + lon0 + '&lat1=' + lat1 + '&lon1=' + lon1 + '&magnetic_north_line=' + mag)
    $.ajax({
        url:'https://xs239613.xsrv.jp/api/mapper?lat0=' + lat0 + '&lon0=' + lon0 + '&lat1=' + lat1 + '&lon1=' + lon1 + '&magnetic_north_line=' + mag,
        type: "GET",

        beforeSend:function(){
            $loading.removeClass("is-hide");
        },
        
        success: function(data){
            
            $loading.addClass("is-hide");

            if (data.datab64 == "too large") {
                html_data = '選択領域が大きすぎます。'
                $("#status").html(html_data);
                $("#image_created").html("");
            } else {
                imgsrc = "data:image/png;base64," + data.datab64;
                console.log(window.outerWidth)
                if (window.outerWidth > 320 ) { 
                    imgwidth = window.outerWidth*2/3; 
                } else { 
                    imgwidth = window.outerWidth;
                }

                $("#status").html("");
                $("#image_created").html('<img style="width: '+imgwidth+'px;" src='+imgsrc+' >')
            }
        }
    });
});