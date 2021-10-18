anychart.onDocumentReady(function() { 
   var fs = require('fs');
   var text = fs.readFileSync("words.txt", 'utf-8');
   var words = text.split('\n');

   var fs = require('fs');
   var text = fs.readFileSync("numbers.txt", 'utf-8');
   var values = text.split('\n');



 var table = [];
 for(var i = 0; i < words.length; i++){
    table.push({"x": words[i], "value": values[i]});
 }
    
    var chart = anychart.tagCloud(table);
    
    chart.title('most common words in an article');
    chart.angles([0, 15, -15, 30, -30]);
    chart.colorRange(true);
    chart.colorRange().length('80%');
    
    chart.container("container");
    chart.draw();
    }); 