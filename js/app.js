$("#create").click(function(){
    var $loading = $(".loading");
    let mag_check = document.getElementById('mag_check');
    let mag;
    
    if ( mag_check.checked) {mag = 'true';}
    else {mag = 'false';}
    
    $.ajax({
        url:'https://xs239613.xsrv.jp/topo/api/mapper?lat0=' + lat0 + '&lon0=' + lon0 + '&lat1=' + lat1 + '&lon1=' + lon1 + '&magnetic_north_line=' + mag,
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
                
                if (window.outerWidth > 320 ) { 
                    imgwidth = window.outerWidth*2/3; 
                } else { 
                    imgwidth = window.outerWidth;
                }

                $("#status").html("");
                $("#image_created").html('<img id="image_file" style="width: '+imgwidth+'px;" src='+imgsrc+' >')
            }
        }
    });
});

$("#netprint").click(function(){

    var $loading = $(".loading");
    var image_file = document.getElementById("image_file") ?? 0;

    if (image_file != 0) {
        
        const file = image_file.src.replace("data:image/png;base64,","");
        const formData = new FormData();

        formData.append('file', new Blob([file], { type: 'text/plain' }), 'tmp.base64');

        $.ajax({
            url: 'https://xs239613.xsrv.jp/topo/api/netprint',
            type: 'post',
            data: formData,
            processData: false,
            contentType: false,

            beforeSend:function(){
                $loading.removeClass("is-hide");
            },

            success: function(data){

                $loading.addClass("is-hide");

                if (data.result =="OK") {
                    let html_data = '<button id="netprint" type="button" class="btn btn-secondary">ネットプリントに登録</button>&nbsp;';
                    html_data += '<a href="https://networkprint.ne.jp/" target="_blank">';
                    html_data += '<img src="img/netprint_rogo.png" width="150px">';
                    html_data += '</a><br>';
                    html_data += 'ユーザー番号: '+data.user_code+' &nbsp;';
                    html_data += '<a href='+data.preview_url+' target="_blank">プレビュー</a>'

                    $("#netprint").html(html_data)

                } else {
                    let html_data = '<button id="netprint" type="button" class="btn btn-secondary">ネットプリントに登録</button>&nbsp;';
                    html_data += '<a href="https://networkprint.ne.jp/" target="_blank">';
                    html_data += '<img src="img/netprint_rogo.png" width="150px">';
                    html_data += '</a><br>';
                    html_data += '登録できませんでした。';

                    $("#netprint").html(html_data)
                }
            }
        });
    
    } else {
        let html_data = '<button id="netprint" type="button" class="btn btn-secondary">ネットプリントに登録</button>&nbsp;';
        html_data += '<a href="https://networkprint.ne.jp/" target="_blank">';
        html_data += '<img src="img/netprint_rogo.png" width="150px">';
        html_data += '</a><br>';
        html_data += '登録する画像を作成してください。';

        $("#netprint").html(html_data)
    }
});