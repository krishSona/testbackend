$(document).ready(function(){
    //upload workers sheet validation
    $("#upload_workers_list").change(function(){
        $('.alert').remove();
        $("#submit_workers_list").removeAttr('disabled')
        var file_input = $('#upload_workers_list')[0];
        if (file_input) {
            var file_chosen = file_input.files[0];
            if (file_chosen) {
                var file_size = file_chosen.size;
                if (file_size > 30000) {
                    var html = "<div class='alert alert-warning alert-dismissible fade show' role='alert'>"
                        html += "File size too large. Maximum 30 KB size file can be uploaded."
                        html += "<button type='button' class='close' data-dismiss='alert' aria-label='Close'>"
                        html += "<span aria-hidden='true'>&times;</span></button></div>"
                        $(".ip_page_title").after(html);
                        $("#submit_workers_list").attr('disabled',true);
                    return false;
                }
            }
        }
        return true;
    });

    //otp timer
    function otp_timer() {
        var seconds = 120;
        $("#time_remaining").html(seconds);
        var x = setInterval(function() {
            seconds -= 1;
            if (seconds < 0) {
                clearInterval(x);
                $(".resendotp_msg").show();
                $(".otp_timer_label").hide();
            } else {
                $("#time_remaining").html(seconds);
            }
        }, 1000);
    }
    //start otp timer
    if ($("#time_remaining").length) {
        otp_timer();
    }
    $("#resend_otp").click(function(){
        $("#otp-form").submit();
    });
});

//app demo
$(document).ready(function(){
    $(".mark").click(function(){
			if (this.classList.contains('attended')) {
				$(this).removeClass('attended')
				var balance = parseInt($('.daily_sal_num').text()) - 200;
			} else {
        $(this).addClass('attended');
        var balance = parseInt($('.daily_sal_num').text()) + 200;
			}
			$('.daily_sal_num').text(balance);
			$('#balance').text(balance);
    });
    $('.deposit_button').click(function(){
        $('.balance_screen').hide();
        $('.confirm_screen').show();
    })
    $('.back_button').click(function(){
        $('.confirm_screen').hide();
        $('.daily_sal_num').text(0);
        $('.balance_screen').show();
    })
});
