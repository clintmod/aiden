var fs = require('fs');
var fileName = process.argv[2]
var newline = "\n";

var output = "";
	fs.readFile(fileName, 'utf8', function (err,data) {
	if (err) {
		return console.log(err);
	}
	var words = data.split(newline)
	for (var i = 0; i < words.length; i++) {
		var word = words[i]
		for (var j = 0; j < word.length; j++) {
			output += word.substring(0,j + 1) + newline;
		}
		output += newline;
	}
	console.log(output)
	fs.writeFile(fileName + ".output.txt", output, 'utf8', function(err) {
		if(err) {
		    return console.log(err);
		}
		console.log("The file was saved to " + fileName + ".output.txt");
	});
});