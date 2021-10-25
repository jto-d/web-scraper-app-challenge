

$.ajax({
   type: "POST",
   url: "~/main.py",
   data: { param: text}
 }).done(function( o ) {
    console.log("yes")
 });

anychart.onDocumentReady(function() { 
 var dict = {"ann":100,
"Courtenay" : 6,
"leighty": 8};


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