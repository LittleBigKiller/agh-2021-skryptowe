var http = require("http");
var fs = require("fs");
const url = require('url');

function requestListener(req, res) {
    console.log("--------------------------------------");
    console.log("The relative URL of the current request: " + req.url + "\n");

    var requrl = new URL(req.url, `http://${req.headers.host}`);

    if (requrl.pathname == '/submit') {
        /* ************************************************** */
        res.writeHead(200, { "Content-Type": "text/plain; charset=utf-8" });
        /* ************************************************** */
        if (req.method == 'GET') {
            var temp = url.parse(req.url, true).query
            var split = temp.cmds.split('\r\n')

            var replstr = ""

            for (elem of split) {
                sp_elem = elem.split(' ')

                if (sp_elem.length == 2) {
                    if (sp_elem[0] == "del") {
                        console.log("del", sp_elem[1])

                        try {
                            fs.unlinkSync(sp_elem[1])
                        } catch (err) {
                            console.error(err)
                            res.end('query failed');
                            return null
                        }

                        replstr += `deleted file ${sp_elem[1]}:\n`

                        try {
                            fs.readdirSync('.').forEach(file => {
                                replstr += file + '\n'
                            })
                        } catch (err) {
                            console.error(err)
                            res.end('query failed');
                            return null
                        }

                        replstr += '\n'
                    }
                }
                // if (sp_elem.length >= 2) {a
                //     if (sp_elem[0] == "mrg") {
                //         console.log("mrg", sp_elem.slice(1))
                //     }
                // }
            }

            console.log(replstr)
            res.end(replstr);
            return null
        }
        else {
            res.write(`This application does not support the ${req.method} method`);
            res.end();
        }
    }
    else {
        res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
        /* ************************************************** */
        res.write(`<form method="GET" action="/submit">
                  <label for="cmds">Input commands</label>
                  <textarea name="cmds" rows="4" cols="50"></textarea>
                  <br>
                  <input type="submit">
                  <input type="reset">
                </form>`);
        /* ************************************************** */
        res.end();
    }
}

/* ************************************************** */
/* Main block
/* ************************************************** */
var server = http.createServer(requestListener); // The 'requestListener' function is defined above
server.listen(8082);
console.log("The server was started on port 8082");
console.log("To stop the server, press 'CTRL + C'");