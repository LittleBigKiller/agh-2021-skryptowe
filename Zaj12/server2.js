function onRequest_8080(request, response) {
  // response.writeHead(200, { "Content-Type": "text/plain" });
  // response.write('Response from 8080\n');
  // response.end();

  fs.stat(file, function (err, stats) {
    if (err == null) { // If the file exists
      fs.readFile(file, function (err, data) { // Read it content
        response.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
        response.write(data);   // Send the content to the web browser
        response.end();
      });
    }
    else { // If the file does not exists
      response.writeHead(200, { "Content-Type": "text/plain; charset=utf-8" });
      response.write(`The '${file}'file does not exist`);
      response.end();
    }
  })
}

function onRequest_8081(request, response) {
  let d = new Date()
  response.writeHead(200, { "Content-Type": "text/xml" });
  response.writeHead(200, { "Access-Control-Allow-Origin": "*" });
  response.write(`<div>
    <span id='date'> ${d.toLocaleDateString()} </span>
    <span id='time'> ${d.toLocaleTimeString()} </span>
  </div>`);
  response.end();
}

/* ************************************************** */
/* Main block
/* ************************************************** */
var http = require('http');
var fs = require("fs");
const file = 'index8080.html';

http.createServer(onRequest_8080).listen(8080);
http.createServer(onRequest_8081).listen(8081);
console.log("The server was started on port 8080 and 8081");
console.log("To stop the server, press 'CTRL + C'");