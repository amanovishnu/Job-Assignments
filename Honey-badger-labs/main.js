// var fs = require('fs');
// var contents = fs.readFileSync('customerdata.txt', 'utf8');
// console.log(contents);
// var textByLine = content.split("\n")
var fs = require('fs');

var args = process.argv.slice(2);
var fileName = args[0];
var text = fs.readFileSync('customerdata.txt', "utf8");
var words = text.split(/\r?\n/);
words = words.map(function (word) { return word.trim() });
words = words.filter(function (word) { return word.length > 0 });
console.log(JSON.stringify(words));