anychart.onDocumentReady(function() { 
 var dict =  {"school": 10,
 "teacher": 4,
 "teachers" : 6,
 "classes" : 7,
 "Klaus": 1,
 "Ms.": 9,
 "Mr. ": 8,
  "homeroom": 2,
  "proud": 3,
  "alumni": 2,
  "today": 5,
  "Coungratulations": 4,
  "South": 3,
  "Jersey": 8,
  "New": 4,
  "UN": 2,
  "Winners" : 1, 
  "beautiful": 1,
  "night": 2,
  "band": 3,
  "buddies" : 1, 
  "freshmen" : 4,
  "sophmores" : 3,
  "juniors": 5,
  "seniors": 6,
  "show": 2,
  "Peer": 2,
  "Leaders" : 3, 
  "barbecue": 1
 };


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

  