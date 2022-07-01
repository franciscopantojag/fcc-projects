var express = require('express');
var cors = require('cors');
const multer = require('multer')
require('dotenv').config()

var app = express();
const upload = multer({ dest: 'uploads/' })

app.use(cors());
app.use('/public', express.static(process.cwd() + '/public'));

app.get('/', function (req, res) {
    res.sendFile(process.cwd() + '/views/index.html');
});

app.post('/api/fileanalyse', upload.single('upfile'), (req, res) => {
  const {originalname:name, mimetype: type, size} = req.file
  return res.status(200).json({
    name, type, size
  })
})


const port = process.env.PORT || 3000;
app.listen(port, function () {
  console.log('Your app is listening on port ' + port)
});
