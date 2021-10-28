
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



anychart.onDocumentReady(function() { 
 


 var table = [];
 for(var key in dict){
    var value = dict[key];
    console.log(value);
    table.push({"x": key, "value": value});

 }
 

    var chart = anychart.tagCloud(table);
    
    chart.title('most common words in an article');
    chart.angles([0, 15, -15, 30, -30]);
    
    
    chart.container("container");
    chart.draw();
    }); 