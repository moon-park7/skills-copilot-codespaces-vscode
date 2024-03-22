// Create web server
var http = require('http');
var url = require('url');
var fs = require('fs');
var qs = require('querystring');
var comments = [];

var server = http.createServer(function(req, res) {
    var parseUrl = url.parse(req.url, true);
    var pathname = parseUrl.pathname;
    if (pathname === '/') {
        fs.readFile('./index.html', function(err, data) {
            if (err) {
                console.log(err);
                res.writeHead(404, {
                    'Content-Type': 'text/html'
                });
                res.end("<h1>404 Not Found</h1>");
            } else {
                res.writeHead(200, {
                    'Content-Type': 'text/html'
                });
                res.end(data);
            }
        });
    } else if (pathname === '/comments') {
        res.writeHead(200, {
            'Content-Type': 'application/json'
        });
        res.end(JSON.stringify(comments));
    } else if (pathname === '/comment') {
        var str = '';
        req.on('data', function(chunk) {
            str += chunk;
        });
        req.on('end', function() {
            var comment = qs.parse(str);
            comments.push(comment);
            res.writeHead(200, {
                'Content-Type': 'application/json'
            });
            res.end(JSON.stringify(comments));
        });
    } else {
        res.writeHead(404, {
            'Content-Type': 'text/html'
        });
        res.end("<h1>404 Not Found</h1>");
    }
});

server.listen(3000, function() {
    console.log('Server is running at http://localhost:3000/');
});