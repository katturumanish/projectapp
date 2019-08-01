var bodyParser = require('body-parser');
var dataitems = [];
//var dataitems = [{item:'machine learning'}, {item:'block chain'}, {item: 'supply chain management'}];
var urlencodedParser = bodyParser.urlencoded({extended: false });

module.exports = function(app){

app.get('/todo', function(req, res){
  res.render('todo', {todos: dataitems});
});

app.post('/todo', urlencodedParser, function(req, res){
  console.log(JSON.stringify(req.body.item))
  var spawn = require("child_process").spawn;
  var process = spawn('python',['/Users/Student/Desktop/testproject.py',
                            req.body.item] );
  //data.push(req.body);
  process.stdout.on('data', function(data){
    console.log(data.toString());
    dataitems.push(data.toString());
    console.log(dataitems);
    console.log(typeof dataitems);
    res.json({todos: dataitems});
    //res.end('end');
  });
});

app.delete('/todo/:item', function(req, res){
  dataitems = dataitems.filter(function(todo){
    return todo.item.replace(/ /g, '-')!== req.params.item;
  });
  res.json({todos: dataitems});
});

}
