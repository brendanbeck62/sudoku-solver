'use strict';

const express = require('express');
const url = require('url');
const favicon = require('express-favicon');
const fs = require('fs');
require('dotenv').config();

// Constants
const PORT = process.env.PORT || 8080;

const app = express();

app.use(express.static(__dirname + '/public/static/'));
app.use(favicon(__dirname + '/public/static/img/favicon.ico'));
app.set('views', __dirname + '/public/views')
app.set('view engine', 'ejs');

app.get(/^(?!\/api\/)/, (req, res) => {
  let purl = url.parse(req.url, true);
  let pathname = 'pages' + purl.pathname;

  if ((pathname)[pathname.length - 1] === '/') {
      pathname += 'index';
  }

  // add the path + extension, so that the fs.access can find it
  var pathPrepend = "./public/views/";
  var extenstion = ".ejs"
  var fullpath = pathPrepend.concat(pathname).concat(extenstion);

  // check if the file exists in the pages directory
  fs.access(fullpath, fs.F_OK, (err) => {
      // if it does not exist, display the 404 page
      if (err) {
          res.render("pages/404", purl.query);
          return
      }

      // otherwise display the page
      res.render(pathname, purl.query);
    })

});

app.listen(PORT, () => {
  console.log(`app listening at http://localhost:${PORT}`)
})