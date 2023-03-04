const express = require('express');
const upload = require('express-fileupload');
const fs = require('fs');
const app = express();

app.use(upload());

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});
// function to get all files from a directory
function getFiles(dir, files_) {
  files_ = files_ || [];
  var files = fs.readdirSync(dir);
  for (var i in files) {
    var name = dir + '/' + files[i];
    if (fs.statSync(name).isDirectory()) {
      getFiles(name, files_);
    } else {
    }
  }
  return files_;
}
app.get('/getFiles', (req, res) => {
  var files = getFiles(__dirname + '/veritas', []);
  res.json({
    status: 200,
    files: files,
  });
});
app.post('/', async (req, res) => {
  if (req.files) {
    // console.log(req.files);
    var file = req.files.Thefile;
    var name = file.name;
    console.log('NAME: ', name);

    file.mv(__dirname + '/veritas/' + name, function (err) {
      if (err) {
        console.log(err);
        res.json({
          status: 500,
          message: 'Error in uploading file',
          error: err,
        });
      } else {
        console.log('File Uploaded');
        res.json({
          status: 200,
          message: 'File Uploaded',
        });
      }
    });
  }
});
var PORT = 5500;
app.listen(PORT, function (err) {
  if (err) console.log('Error in server setup');
  console.log('Server listening on Port', PORT);
});
