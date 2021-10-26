$(function(){
	$('button').click(function(){
		var url = $('#inputURL').val();
        var encoded = encodeURIComponent(encodeURIComponent(url))
		$.ajax({
			url: 'http://127.0.0.1:5000/webpage/' + encoded,
			data: $('form').serialize(),
			type: 'GET',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});